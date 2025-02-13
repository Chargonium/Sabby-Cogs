from redbot.core import commands
import random

class SigmaCheck(commands.Cog):
    """A simple ping command cog."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sigmacheck(self, ctx):
        """Replies with the user's sigma percentage!"""
        percentage = random.randint(0, 100)

        args = ctx.message.content.split(" ")

        if len(args) >= 2:
            pinged_id = args[1].removeprefix("<@").removesuffix(">")
            try:
                pinged_id = int(pinged_id)
                user = ctx.guild.get_member(pinged_id)
                if user is None:
                    await ctx.send("Invalid user")
                    return
                
                if percentage >= 60:
                    await ctx.send(f"Wow, <@{pinged_id}> is super sigma with {percentage}%")
                    return
                elif percentage < 60 and percentage >= 10:
                    await ctx.send(f"<@{pinged_id}> is {percentage}% sigma!")
                    return
                elif percentage < 10:
                    await ctx.send(f"<@{pinged_id}> is not sigma bro")
                    return
            except:
                await ctx.send("Invalid user")
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
    async def rizzcheck(self, ctx):
        """Replies with the user's rizz!"""

        percentage = random.randint(0, 100)

        args = ctx.message.content.split(" ")

        if len(args) >= 2:
            pinged_id = args[1].removeprefix("<@").removesuffix(">")
            try:
                pinged_id = int(pinged_id)
                user = ctx.guild.get_member(pinged_id)
                if user is None:
                    await ctx.send("Invalid user")
                    return
                
                if percentage >= 60:
                    await ctx.send(f"<@{pinged_id}> is the rizzler with {percentage}%")
                    return
                elif percentage < 60 and percentage >= 10:
                    await ctx.send(f"<@{pinged_id}> has {percentage}% rizz")
                    return
                elif percentage < 10:
                    await ctx.send(f"<@{pinged_id}> has -{percentage}% rizz")
                    return
            except:
                await ctx.send("Invalid user")
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

def setup(bot):
    bot.add_cog(SigmaCheck(bot))