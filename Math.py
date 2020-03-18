

import discord
from discord.ext import commands


class Math(commands.Cog):

	def __init__(self, bot):


		self.bot = bot


	@commands.command(aliases= ['+'])

	async def calc_p(self, ctx, n1:int,n2:int):



		SUM = n1 + n2

		await ctx.send(f'''
		
		`INPUT` : `{n1} + {n2} `
		
`OUTPUT` : `{SUM}`
		''')


	@commands.command(aliases= ['x'])

	async def calc_mul(self, ctx, n1:int,n2:int):



		SUM = n1 * n2

		await ctx.send(f'''
		
		`INPUT` : `{n1} x {n2} `
		
`OUTPUT` : `{SUM}`
		''')
		

	@commands.command(aliases= ['-'])

	async def calc_mi(self, ctx, n1:int,n2:int):



		SUM = n1 - n2

		await ctx.send(f'''
		
		`INPUT` : `{n1} - {n2} `
		
`OUTPUT` : `{SUM}`
		''')


	@commands.command(aliases= ['/'])

	async def calc_de(self, ctx, n1:int,n2:int):



		SUM = (n1) / (n2)

		await ctx.send(f'''
		
		`INPUT` : `{n1} : {n2} `
		
`OUTPUT` : `{SUM}`
		''')
		

	
	@commands.command(aliases= ['^'])

	async def calc_sq(self, ctx, n1:int,n2:int):



		SUM = n1 ** n2

		await ctx.send(f'''
		
		`INPUT` : `{n1} ** {n2} `
		
`OUTPUT` : `{SUM}`
		''')
		

		


	@commands.command()

	async def _countTo(self, ctx, *,counter=None):

		if counter is None:

			await ctx.send(f'Amount?')

		else:

			count = 1

			while count <= int(counter):

				await ctx.send(f'`{count}` : `{counter}`')
				count += 1


def setup(bot):

	bot.add_cog(Math(bot))
 
