import asyncio
import os
import logging
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

# 配置日志
logging.basicConfig(level=logging.INFO)

def load_config() -> tuple:
    """加载环境变量并返回API Key和Base URL"""
    load_dotenv(override=True)
    set_tracing_disabled(True)

    api_key = os.getenv('DEEPSEEK_API_KEY')
    base_url = os.getenv('BASE_URL')

    if not api_key:
        logging.error('未找到DEEPSEEK_API_KEY，请检查.env文件')
        raise ValueError('未找到DEEPSEEK_API_KEY，请检查.env文件')

    return api_key, base_url

async def main() -> None:
    """主函数"""
    deepseek_api_key, deepseek_base_url = load_config()

    set_default_openai_api('chat_completions')

    deepseek_client = AsyncOpenAI(
        api_key=deepseek_api_key,
        base_url=deepseek_base_url,
    )

    set_default_openai_client(deepseek_client, use_for_tracing=False)

    agent = Agent(
        name='DeepSeek Assistant',
        instructions='你是一个有帮助的助手，请用中文回答',
        model=OpenAIChatCompletionsModel(
            model="deepseek-v4-flash",
            openai_client=deepseek_client,
        )
    )

    result = await Runner.run(agent, '你好，1+1等于多少')
    print(result.final_output)

if __name__ == '__main__':
    asyncio.run(main())
