import asyncio
import os
from dotenv import load_dotenv

from openai import AsyncOpenAI

from agents import (
    Agent,
    Runner,
    set_default_openai_client,
    set_default_openai_api,
    set_tracing_disabled,
    OpenAIChatCompletionsModel,
)

# 1、加载环境变量
load_dotenv(override=True)

# 2、关闭追踪
set_tracing_disabled(True)

# 3、从环境变量中读取API Key
deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')
if not deepseek_api_key:
    raise ValueError('没找到DEEPSEEK_API_KEY,请检查.env文件')
deepseek_base_url = os.getenv('BASE_URL')

# 4、DeepSeek 只支持 Chat Completions API，需要显式指定
set_default_openai_api('chat_completions')

# 5、创建兼容OpenAI格式的deepseek客户端
deepseek_client = AsyncOpenAI(
    api_key=deepseek_api_key,
    base_url=deepseek_base_url,
)

# 6、把自定义客户端设为sdk默认使用的客户端,use_for_tracing=False阻止了追踪功能使用该客户端的API密钥但没有关闭追踪。
set_default_openai_client(deepseek_client, use_for_tracing=False)


async def main():
    # 7、定义Agent并指定用 OpenAIChatCompletionsModel包装Deepseek模型
    agent = Agent(
        name='DeepSeek Assistant',
        instructions='你是一个有帮助的助手，请用中文回答',
        # 上面有set_default_openai_api('chat_completions')，可以不要OpenAIChatCompletionsModel，直接model="deepseek-v4-flash"
        model=OpenAIChatCompletionsModel(
            model="deepseek-v4-flash",
            openai_client=deepseek_client,
        )
    )

    # print(type(agent))
    # print(agent)

    # 8、运行agent
    result = await Runner.run(agent, '你好，1+1等于多少')
    print(result.final_output)

if __name__ == '__main__':
    asyncio.run(main())
