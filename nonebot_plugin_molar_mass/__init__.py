from nonebot import on_command, logger
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11.message import Message

from .calc import calc


molar_mass = on_command('摩尔质量', aliases={'相对分子质量'})


@molar_mass.handle()
async def handle_receive_molar_mass(arg: Message = CommandArg()):
    chemical = arg.extract_plain_text()
    try:
        await molar_mass.finish(str(calc(chemical)))
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e}')
        await molar_mass.finish('计算出错，请检查输入格式')


__all__ = []
