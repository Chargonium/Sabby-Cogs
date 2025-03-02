import discord
from redbot.core import commands
import random

class SigmaCheck(commands.Cog):
    """This cog is 101% sigma."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["sigma"])
    async def sigmacheck(self, ctx, user: discord.User = None):
        """Gets someone's sigma level"""

        percentage = random.randint(0, 100) # gets the sigma level using a top secret method (definitly not just randomly generated)

        if user:
                
            if percentage >= 75:
                await ctx.send(f"Wow, {user.mention} is super sigma with {percentage}%")
                return
            elif percentage >= 10:
                await ctx.send(f"{user.mention} is {percentage}% sigma!")
                return
            elif percentage < 10:
                await ctx.send(f"{user.mention} is not sigma bro")
                return

        else:
            if percentage >= 75:
                await ctx.send(f"Wow, you super sigma with {percentage}%")
                return
            elif percentage >= 10:
                await ctx.send(f"You are {percentage}% sigma!")
                return
            elif percentage < 10:
                await ctx.send(f"You're not sigma bro")
                return
        await ctx.send("you're so not sigma that the bot broke ):")

    @commands.command(aliases=["rizz"])
    async def rizzcheck(self, ctx, user: discord.User = None):
        """Gets someone's rizz level!"""

        percentage = random.randint(0, 100) # gets the rizz level using a top secret method (definitly not just randomly generated)

        if user:
            if percentage >= 75:
                await ctx.send(f"{user.mention} is the rizzler with {percentage}%")
                return
            elif percentage >= 10:
                await ctx.send(f"{user.mention} has {percentage}% rizz")
                return
            elif percentage < 10:
                await ctx.send(f"{user.mention} has -{percentage}% rizz")
                return
        else:
            if percentage >= 75:
                await ctx.send(f"You're the rizzler with {percentage}%")
                return
            elif percentage >= 10:
                await ctx.send(f"You have {percentage}% rizz")
                return
            elif percentage < 10:
                await ctx.send(f"You got -{percentage}% rizz")
                return
        await ctx.send("your rizz is so low the bot broke ):")

    @commands.command(aliases=["vibe"])
    async def vibecheck(self, ctx, user: discord.User = None):
        """Checks someone's vibe"""
        
        percentage = random.randint(0, 100) # gets the vibe level using a top secret method (definitly not just randomly generated)

        if user:
                
            if percentage >= 75:
                await ctx.send(f"{user.mention} passed the vibe check with {percentage}%")
                return
            elif percentage >= 10:
                await ctx.send(f"{user.mention} has {percentage}% vibe!")
                return
            elif percentage < 10:
                await ctx.send(f"{user.mention} didn't pass the vibe check")
                return

        else:
            if percentage >= 75:
                await ctx.send(f"You passed the vibe check with {percentage}%")
                return
            elif percentage >= 10:
                await ctx.send(f"You have {percentage}% vibe!")
                return
            elif percentage < 10:
                await ctx.send(f"You didn't pass the vibe check")
                return
        await ctx.send("your vibe is so low that the bot broke ):")

async def setup(bot: commands.Bot):
    await bot.add_cog(SigmaCheck(bot))