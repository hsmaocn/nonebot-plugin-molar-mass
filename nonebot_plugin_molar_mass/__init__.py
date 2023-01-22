from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import Matcher, CommandArg, ArgPlainText, CommandStart

from .calc import calc


molar_mass = on_command('摩尔质量', aliases={'相对分子质量'})


@molar_mass.handle()
async def handle_receive_molar_mass(matcher: Matcher, arg: Message = CommandArg()):
    if arg.extract_plain_text():
        matcher.set_arg('chemical', arg)


@molar_mass.got('chemical', prompt='你想计算哪个物质？')
async def handle_calc_molar_mass(chemical_name: str = ArgPlainText('chemical'), name: Message = CommandStart()):
    name = name.extract_plain_text()

    try:
        result = calc(chemical_name)
        await molar_mass.finish(f'{chemical_name}的{name}是{result}')
    except (NameError, ValueError) as e:
        await molar_mass.reject(f'计算出错: {e}')


__all__ = []
