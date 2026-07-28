"""
OpenAI Agents SDK - Skills（技能/工具）使用示例

在 OpenAI Agents SDK 中，"Skills" 通过 Function Tools（函数工具）实现。
本示例演示：
1. 使用 @tool 装饰器定义技能（函数工具）
2. 多个技能组合到一个 Agent
3. 使用 RunContextWrapper 传递上下文
4. Agents as tools（智能体作为工具）
"""

import asyncio
import os
import json
from typing import Any
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import (
    Agent,
    Runner,
    set_default_openai_client,
    set_default_openai_api,
    set_tracing_disabled,
    OpenAIChatCompletionsModel,
    RunContextWrapper,
    function_tool,
)

# ==================== 1. 环境配置 ====================

load_dotenv(override=True)
set_tracing_disabled(True)

deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')
if not deepseek_api_key:
    raise ValueError('未找到 DEEPSEEK_API_KEY，请检查 .env 文件')
deepseek_base_url = os.getenv('BASE_URL')

set_default_openai_api('chat_completions')

deepseek_client = AsyncOpenAI(
    api_key=deepseek_api_key,
    base_url=deepseek_base_url,
)

set_default_openai_client(deepseek_client, use_for_tracing=False)


# ==================== 2. 定义技能（Function Tools） ====================

# --- 技能1: 查询天气 ---
@function_tool
def get_weather(city: str) -> str:
    """查询指定城市的天气信息。

    Args:
        city: 城市名称，例如 "北京"、"上海"。
    """
    # 模拟天气数据（实际项目中可调用天气API）
    weather_data = {
        "北京": "晴天，气温 28°C，湿度 45%",
        "上海": "多云，气温 30°C，湿度 70%",
        "广州": "小雨，气温 26°C，湿度 85%",
        "深圳": "阴天，气温 27°C，湿度 75%",
    }
    return weather_data.get(city, f"{city}：暂无天气数据，请稍后重试。")


# --- 技能2: 计算数学表达式 ---
@function_tool
def calculate(expression: str) -> str:
    """计算数学表达式并返回结果。

    Args:
        expression: 数学表达式，例如 "2 + 3 * 4"。
    """
    try:
        # 安全地计算数学表达式
        allowed_chars = set("0123456789+-*/.() ")
        if not all(c in allowed_chars for c in expression):
            return "错误：表达式包含不允许的字符。"
        result = eval(expression)  # 已做字符白名单过滤
        return f"{expression} = {result}"
    except Exception as e:
        return f"计算错误：{e}"


# --- 技能3: 查询用户信息（带上下文） ---
@function_tool
def get_user_info(ctx: RunContextWrapper[Any], user_id: str) -> str:
    """根据用户ID查询用户信息。需要上下文中的用户数据库。

    Args:
        user_id: 用户ID，例如 "U001"。
    """
    # 从上下文中获取用户数据库
    user_db = ctx.context.get("user_db", {})
    user = user_db.get(user_id)
    if user:
        return json.dumps(user, ensure_ascii=False, indent=2)
    return f"未找到用户ID为 {user_id} 的记录。"


# --- 技能4: 记录日志 ---
@function_tool
def log_event(ctx: RunContextWrapper[Any], event: str) -> str:
    """记录一个事件到日志系统。

    Args:
        event: 要记录的事件描述。
    """
    # 将事件追加到上下文中的日志列表
    if "event_log" not in ctx.context:
        ctx.context["event_log"] = []
    ctx.context["event_log"].append(event)
    return f"已记录事件：{event}"


# ==================== 3. 示例一：基础技能使用 ====================

async def demo_basic_skills():
    """演示基础技能：将多个函数工具组合到一个 Agent"""
    print("=" * 50)
    print("示例一：基础技能使用")
    print("=" * 50)

    agent = Agent(
        name='技能助手',
        instructions='你是一个有用的助手，可以查询天气和进行数学计算。请用中文回答。',
        model=OpenAIChatCompletionsModel(
            model="deepseek-v4-flash",
            openai_client=deepseek_client,
        ),
        tools=[get_weather, calculate],  # 注册技能
    )

    # 测试天气查询技能
    result = await Runner.run(agent, '北京今天天气怎么样？')
    print(f"天气查询结果：{result.final_output}\n")

    # 测试数学计算技能
    result = await Runner.run(agent, '帮我算一下 (125 + 375) * 2 / 5 等于多少？')
    print(f"计算结果：{result.final_output}\n")


# ==================== 4. 示例二：带上下文的技能 ====================

async def demo_context_skills():
    """演示带上下文的技能：通过 context 传递外部数据"""
    print("=" * 50)
    print("示例二：带上下文的技能")
    print("=" * 50)

    # 准备上下文数据
    context = {
        "user_db": {
            "U001": {"姓名": "张三", "年龄": 28, "部门": "技术部", "职位": "高级工程师"},
            "U002": {"姓名": "李四", "年龄": 32, "部门": "产品部", "职位": "产品经理"},
            "U003": {"姓名": "王五", "年龄": 25, "部门": "设计部", "职位": "UI设计师"},
        },
        "event_log": [],
    }

    agent = Agent(
        name='用户管理助手',
        instructions='你是一个用户管理助手，可以查询用户信息和记录事件。请用中文回答。',
        model=OpenAIChatCompletionsModel(
            model="deepseek-v4-flash",
            openai_client=deepseek_client,
        ),
        tools=[get_user_info, log_event],  # 注册技能
    )

    # 查询用户信息
    result = await Runner.run(
        agent,
        '请帮我查一下 U002 的信息',
        context=context,  # 传入上下文
    )
    print(f"用户查询结果：{result.final_output}\n")

    # 查看记录的日志
    print(f"事件日志：{context['event_log']}\n")


# ==================== 5. 示例三：Agents as Tools（智能体作为技能） ====================

async def demo_agents_as_tools():
    """演示 Agents as Tools：将一个 Agent 作为另一个 Agent 的工具"""
    print("=" * 50)
    print("示例三：智能体作为技能（Agents as Tools）")
    print("=" * 50)

    # 子智能体1：翻译专家
    translator_agent = Agent(
        name='翻译专家',
        instructions='你是一个专业的中英翻译员。当收到中文时翻译成英文，收到英文时翻译成中文。只输出翻译结果，不要多余解释。',
        model=OpenAIChatCompletionsModel(
            model="deepseek-v4-flash",
            openai_client=deepseek_client,
        ),
    )

    # 子智能体2：摘要专家
    summarizer_agent = Agent(
        name='摘要专家',
        instructions='你是一个文本摘要专家。请将给定的文本压缩为简洁的摘要，保留关键信息。请用中文回答。',
        model=OpenAIChatCompletionsModel(
            model="deepseek-v4-flash",
            openai_client=deepseek_client,
        ),
    )

    # 主智能体：将子智能体作为工具使用
    from agents import Agent, Runner

    coordinator = Agent(
        name='协调助手',
        instructions=(
            '你是一个协调助手，可以根据用户需求调用翻译专家或摘要专家。'
            '如果用户要求翻译，调用翻译专家；如果用户要求总结或摘要，调用摘要专家。'
            '请用中文回答。'
        ),
        model=OpenAIChatCompletionsModel(
            model="deepseek-v4-flash",
            openai_client=deepseek_client,
        ),
        tools=[
            translator_agent.as_tool(
                tool_name="translate",
                tool_description="调用翻译专家进行中英互译",
            ),
            summarizer_agent.as_tool(
                tool_name="summarize",
                tool_description="调用摘要专家生成文本摘要",
            ),
        ],
    )

    # 测试翻译技能
    result = await Runner.run(coordinator, '请把以下内容翻译成英文："人工智能正在改变我们的生活方式"')
    print(f"翻译结果：{result.final_output}\n")

    # 测试摘要技能
    long_text = (
        "人工智能（AI）是计算机科学的一个分支，致力于创建能够执行通常需要人类智能的任务的系统。"
        "这些任务包括视觉感知、语音识别、决策制定和语言翻译。"
        "近年来，深度学习的突破使得AI技术在图像识别、自然语言处理、推荐系统等领域取得了显著进展。"
        "AI已经广泛应用于医疗诊断、自动驾驶、金融分析等行业，正在深刻改变我们的工作和生活方式。"
    )
    result = await Runner.run(coordinator, f'请帮我总结以下内容：\n{long_text}')
    print(f"摘要结果：{result.final_output}\n")


# ==================== 主函数 ====================

async def main():
    """运行所有示例"""
    # 示例一：基础技能
    await demo_basic_skills()

    # 示例二：带上下文的技能
    await demo_context_skills()

    # 示例三：智能体作为技能
    await demo_agents_as_tools()


if __name__ == '__main__':
    asyncio.run(main())
