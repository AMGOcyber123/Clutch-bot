import discord
from discord.ext import commands
client = commands.Bot(command_prefix="!")
@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name+" Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server id", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member_count",value=memberCount,inline=True)

    await ctx.send(embed=embed)
client.run('Nzc0MjExMDM5NzUxNDM4MzM2.X6UeOA.c9axHlKkqDnivlYtbiFV1hq69W0')