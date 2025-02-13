import discord
from redbot.core import commands
import random

class SigmaCheck(commands.Cog):
    """This cog is 101% sigma."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sigmacheck(self, ctx, user: discord.User = None):
        """Replies with the user's sigma percentage!"""
        percentage = random.randint(0, 100)

        if user:
                
            if percentage >= 60:
                await ctx.send(f"Wow, {user.mention} is super sigma with {percentage}%")
                return
            elif percentage < 60 and percentage >= 10:
                await ctx.send(f"{user.mention} is {percentage}% sigma!")
                return
            elif percentage < 10:
                await ctx.send(f"{user.mention} is not sigma bro")
                return

        else:
            if percentage >= 60:
                await ctx.send(f"Wow, you super sigma with {percentage}%")
                return
            elif percentage < 60 and percentage >= 10:
                await ctx.send(f"You are {percentage}% sigma!")
                return
            elif percentage < 10:
                await ctx.send(f"You're not sigma bro")
                return
        await ctx.send("you're so not sigma that the bot broke ):")

    @commands.command()
    async def rizzcheck(self, ctx, user: discord.User = None):
        """Replies with the user's rizz!"""

        percentage = random.randint(0, 100)

        if user:
            if percentage >= 60:
                await ctx.send(f"{user.mention} is the rizzler with {percentage}%")
                return
            elif percentage < 60 and percentage >= 10:
                await ctx.send(f"{user.mention} has {percentage}% rizz")
                return
            elif percentage < 10:
                await ctx.send(f"{user.mention} has -{percentage}% rizz")
                return
        else:
            if percentage >= 60:
                await ctx.send(f"You're the rizzler with {percentage}%")
                return
            elif percentage < 60 and percentage >= 10:
                await ctx.send(f"You have {percentage}% rizz")
                return
            elif percentage < 10:
                await ctx.send(f"You got -{percentage}% rizz")
                return
        await ctx.send("your rizz is so low the bot broke ):")

async def setup(bot):
    await bot.add_cog(SigmaCheck(bot))