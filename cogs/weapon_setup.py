import discord
from discord.ext import commands


class Weapon(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Weapon COMMAND
    @commands.command()
    async def weapon(self, ctx, *, name):
        channel = self.client.get_channel(845246215796424704)
        # AK-47
        if name == 'AK-47' or name == 'ak-47':
            details = discord.Embed(
                title='Weapon: AK-47',
                description='Powerful and reliable, the AK-47 is one of the most popular assault' +
                'rifles in the world. It is most deadly in short, controlled bursts of fire.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/ak-47-714163b7deae61b72d41d3b9c3cd8385.png')
            details.add_field(name='TYPE', value='Rifle', inline=True)
            details.add_field(name='INGAME PRICE', value='$2700', inline=True)
            details.add_field(name='FIRE RATE',
                              value='600 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='Terrorists', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='2.5 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='22 M', inline=True)
            details.add_field(name='MODE', value='Automatic', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='30/90', inline=True)
            details.add_field(
                name='SPRAY PATTERN', value='https://leetify.com/academy/csgo-spray-patterns#ak47', inline=False)
            await channel.send(embed=details)

        # AWP
        elif name == 'AWP' or name == 'awp':
            details = discord.Embed(
                title='Weapon: AWP',
                description='High risk and high reward, the infamous AWP is recognizable by its signature report and one-shot, one-kill policy.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/awp-32e573c62ed3339057f40af051a63070.png')
            details.add_field(name='TYPE', value='Sniper Rifle', inline=True)
            details.add_field(name='INGAME PRICE', value='$4750', inline=True)
            details.add_field(name='FIRE RATE',
                              value='41 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='CT/T(Both)', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='3.7 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='69 M', inline=True)
            details.add_field(name='MODE', value='Bolt Action', inline=True)
            details.add_field(name='KILL AWARD', value='$50/$100', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='10/30', inline=True)
            await channel.send(embed=details)

        # M4A4
        elif name == 'M4A4' or name == 'm4a4':
            details = discord.Embed(
                title='Weapon: M4A4',
                description='More accurate but less damaging than its AK-47 counterpart, the M4A4 is the full-auto assault rifle of choice for CTs.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/m4a4-c112a80f9f8466cb1f78237cc794c692.png')
            details.add_field(name='TYPE', value='Rifle', inline=True)
            details.add_field(name='INGAME PRICE', value='$3100', inline=True)
            details.add_field(name='FIRE RATE',
                              value='666 SHOTS/MIN', inline=True)
            details.add_field(
                name='SIDE', value='Counter-Terrorists', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='3.1 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='28 M', inline=True)
            details.add_field(name='MODE', value='Automatic', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='30/90', inline=True)
            details.add_field(
                name='SPRAY PATTERN', value='https://leetify.com/academy/csgo-spray-patterns#m4a4', inline=False)
            await channel.send(embed=details)

        # M4A1-S
        elif name == 'M4A1-S' or name == 'm4a1-s':
            details = discord.Embed(
                title='Weapon: M4A1-S',
                description='With a smaller magazine than its unmuffled counterpart, the silenced M4A1 provides quieter ' +
                'shots with less recoil and better accuracy.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/m4a1-s-232b8838186ff35d3ba94dca97d2da64.png')
            details.add_field(name='TYPE', value='Rifle', inline=True)
            details.add_field(name='INGAME PRICE', value='$2900', inline=True)
            details.add_field(name='FIRE RATE',
                              value='600 SHOTS/MIN', inline=True)
            details.add_field(
                name='SIDE', value='Counter-Terrorists', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='3.1 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='28 M', inline=True)
            details.add_field(name='MODE', value='Automatic', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='25/75', inline=True)
            details.add_field(
                name='SPRAY PATTERN', value='https://leetify.com/academy/csgo-spray-patterns#m4a1-s', inline=False)
            await channel.send(embed=details)

        # AUG
        elif name == 'AUG' or name == 'aug':
            details = discord.Embed(
                title='Weapon: AUG',
                description='Powerful and accurate, the AUG scoped assault rifle compensates for its long reload times ' +
                'with low spread and a high rate of fire',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/aug-748c88a7052892c6dee52c7e2e86eac4.png')
            details.add_field(name='TYPE', value='Rifle', inline=True)
            details.add_field(name='INGAME PRICE', value='$3300', inline=True)
            details.add_field(name='FIRE RATE',
                              value='666 SHOTS/MIN', inline=True)
            details.add_field(
                name='SIDE', value='Counter-Terrorists', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='3.8 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='35 M', inline=True)
            details.add_field(name='MODE', value='Automatic', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='30/90', inline=True)
            details.add_field(
                name='SPRAY PATTERN', value='https://leetify.com/academy/csgo-spray-patterns#aug', inline=False)
            await channel.send(embed=details)

        # SG 553
        elif name == 'SG 553' or name == 'sg 553':
            details = discord.Embed(
                title='Weapon: SG 553',
                description='The terrorist-exclusive SG 553 is a premium scoped alternative to the AK-47 for effective long-range engagement.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/sg-553-9e71282877e8132318c33ff26848813a.png')
            details.add_field(name='TYPE', value='Rifle', inline=True)
            details.add_field(name='INGAME PRICE', value='$3000', inline=True)
            details.add_field(name='FIRE RATE',
                              value='666 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='Terrorists', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='2.8 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='36 M', inline=True)
            details.add_field(name='MODE', value='Automatic', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='30/90', inline=True)
            details.add_field(
                name='SPRAY PATTERN', value='https://leetify.com/academy/csgo-spray-patterns#sg-553', inline=False)
            await channel.send(embed=details)

        # GALIL AR
        elif name == 'GALIL AR' or name == 'galil ar':
            details = discord.Embed(
                title='Weapon: GALIL AR',
                description='A less expensive option among the terrorist-exclusive assault rifles, the Galil AR is a ' +
                'serviceable weapon in medium to long-range combat.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/galil-ar-f1a45f1856155071c3ad8718d0012ba4.png')
            details.add_field(name='TYPE', value='Rifle', inline=True)
            details.add_field(name='INGAME PRICE', value='$2000', inline=True)
            details.add_field(name='FIRE RATE',
                              value='666 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='Terrorists', inline=True)
            details.add_field(name='RELOAD TIME', value='3 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='16 M', inline=True)
            details.add_field(name='MODE', value='Automatic', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='35/90', inline=True)
            details.add_field(
                name='SPRAY PATTERN', value='https://leetify.com/academy/csgo-spray-patterns#galil', inline=False)
            await channel.send(embed=details)

        # FAMAS
        elif name == 'FAMAS' or name == 'famas':
            details = discord.Embed(
                title='Weapon: FAMAS',
                description='A cheap option for cash-strapped players, the FAMAS effectively fills the ' +
                'niche between more expensive rifles and the less-effective SMGs.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/famas-7b4fe9e5303c1af142ff84dc381818f7.png')
            details.add_field(name='TYPE', value='Rifle', inline=True)
            details.add_field(name='INGAME PRICE', value='$2250', inline=True)
            details.add_field(name='FIRE RATE',
                              value='666 SHOTS/MIN', inline=True)
            details.add_field(
                name='SIDE', value='Counter-Terrorists', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='3.3 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='15 M', inline=True)
            details.add_field(name='MODE', value='Auto/Burst', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='25/90', inline=True)
            details.add_field(
                name='SPRAY PATTERN', value='https://leetify.com/academy/csgo-spray-patterns#famas', inline=False)
            await channel.send(embed=details)

        # SSG 08
        elif name == 'SSG 08' or name == 'ssg 08':
            details = discord.Embed(
                title='Weapon: SSG 08',
                description='The SSG 08 bolt-action is a low-damage but very cost-effective sniper rifle, making it ' +
                'a smart choice for early-round long-range marksmanship.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/ssg-08-bdb511427503d3fddf28e2309b754594.png')
            details.add_field(name='TYPE', value='Sniper Rifle', inline=True)
            details.add_field(name='INGAME PRICE', value='$1700', inline=True)
            details.add_field(name='FIRE RATE',
                              value='48 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='CT/T(Common)', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='3.7 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='47 M', inline=True)
            details.add_field(name='MODE', value='Bolt Action', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='10/90', inline=True)
            await channel.send(embed=details)

        # SCAR-20
        elif name == 'SCAR-20' or name == 'scar-20':
            details = discord.Embed(
                title='Weapon: SCAR-20',
                description='The SCAR-20 is a semi-automatic sniper rifle that trades a high rate of fire and ' +
                'powerful long-distance damage for sluggish movement speed and big price tag.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/scar-20-50f6612f7dfe8132760777172dd4c369.png')
            details.add_field(name='TYPE', value='Sniper Rifle', inline=True)
            details.add_field(name='INGAME PRICE', value='$5000', inline=True)
            details.add_field(name='FIRE RATE',
                              value='240 SHOTS/MIN', inline=True)
            details.add_field(
                name='SIDE', value='Counter-Terrorists', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='3.1 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='66 M', inline=True)
            details.add_field(name='MODE', value='Automatic', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='20/90', inline=True)
            await channel.send(embed=details)

        # G3SG1
        elif name == 'G3SG1' or name == 'g3sg1':
            details = discord.Embed(
                title='Weapon: G3SG1',
                description='The pricy G3SG1 lowers movement speed considerably but compensates with ' +
                'a higher rate of fire than other sniper rifles.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/g3sg1-91a12760cf0526a595e644d6e5b2e9c7.png')
            details.add_field(name='TYPE', value='Sniper Rifle', inline=True)
            details.add_field(name='INGAME PRICE', value='$5000', inline=True)
            details.add_field(name='FIRE RATE',
                              value='240 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='Terrorists', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='4.7 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='66 M', inline=True)
            details.add_field(name='MODE', value='Automatic', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='20/90', inline=True)
            await channel.send(embed=details)

        # P90
        elif name == 'P90' or name == 'p90':
            details = discord.Embed(
                title='Weapon: P90',
                description='Easily recognizable for its unique bullpup design, the P90 is a great weapon ' +
                'to shoot on the move due to its high-capacity magazine and low recoil.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/p90-ce0cfa771ecd9f1c2946f4ad3ac963b2.png')
            details.add_field(name='TYPE', value='SMG', inline=True)
            details.add_field(name='INGAME PRICE', value='$2350', inline=True)
            details.add_field(name='FIRE RATE',
                              value='857 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='CT/T(Common)', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='3.3 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='10 M', inline=True)
            details.add_field(name='MODE', value='Automatic', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='50/100', inline=True)
            details.add_field(
                name='SPRAY PATTERN', value='https://leetify.com/academy/csgo-spray-patterns#p90', inline=False)
            await channel.send(embed=details)

        # UMP-45
        elif name == 'UMP-45' or name == 'ump-45':
            details = discord.Embed(
                title='Weapon: UMP-45',
                description="The misunderstood middle child of the SMG family, the UMP45's small magazine " +
                "is the only drawback to an otherwise versatile close-quarters automatic.",
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/ump-45-564c1d13e98901485abc0ddd94aaf5fa.png')
            details.add_field(name='TYPE', value='SMG', inline=True)
            details.add_field(name='INGAME PRICE', value='$1200', inline=True)
            details.add_field(name='FIRE RATE',
                              value='666 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='CT/T(Common)', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='3.5 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='11 M', inline=True)
            details.add_field(name='MODE', value='Automatic', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$300/$600', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='25/100', inline=True)
            details.add_field(
                name='SPRAY PATTERN', value='https://leetify.com/academy/csgo-spray-patterns#ump-45', inline=False)
            await channel.send(embed=details)

        # MAC-10
        elif name == 'MAC-10' or name == 'mac-10':
            details = discord.Embed(
                title='Weapon: MAC-10',
                description='Essentially a box that bullets come out of, the MAC-10 SMG boasts a high rate of fire, ' +
                'with poor spread accuracy and high recoil as trade-offs.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/mac-10-d9795dc5aec15ceb7716dbb6901d9b2e.png')
            details.add_field(name='TYPE', value='SMG', inline=True)
            details.add_field(name='INGAME PRICE', value='$1050', inline=True)
            details.add_field(name='FIRE RATE',
                              value='800 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='Terrorists', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='2.6 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='11 M', inline=True)
            details.add_field(name='MODE', value='Automatic', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$300/$600', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='30/100', inline=True)
            details.add_field(
                name='SPRAY PATTERN', value='https://leetify.com/academy/csgo-spray-patterns#mac-10', inline=False)
            await channel.send(embed=details)

        # MP7
        elif name == 'MP7' or name == 'mp7':
            details = discord.Embed(
                title='Weapon: MP7',
                description='Versatile but expensive, the German-made MP7 SMG is the perfect choice for high-impact close-range combat.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/mp7-e49667aca179260ac5567cc4c92c7a49.png')
            details.add_field(name='TYPE', value='SMG', inline=True)
            details.add_field(name='INGAME PRICE', value='$1500', inline=True)
            details.add_field(name='FIRE RATE',
                              value='750 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='CT/T(Common)', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='3.1 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='14 M', inline=True)
            details.add_field(name='MODE', value='Automatic', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$300/$600', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='30/120', inline=True)
            details.add_field(
                name='SPRAY PATTERN', value='https://leetify.com/academy/csgo-spray-patterns#mp7', inline=False)
            await channel.send(embed=details)

        # MP9
        elif name == 'MP9' or name == 'mp9':
            details = discord.Embed(
                title='Weapon: MP9',
                description='Manufactured in Switzerland, the cutting-edge MP9 SMG is an ergonomic polymer weapon favored by private security firms.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/mp9-06e32e5e74001f4c66a36519f01d8ffd.png')
            details.add_field(name='TYPE', value='SMG', inline=True)
            details.add_field(name='INGAME PRICE', value='$1250', inline=True)
            details.add_field(name='FIRE RATE',
                              value='857 SHOTS/MIN', inline=True)
            details.add_field(
                name='SIDE', value='Counter-Terrorists', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='2.1 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='16 M', inline=True)
            details.add_field(name='MODE', value='Automatic', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$300/$600', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='30/120', inline=True)
            details.add_field(
                name='SPRAY PATTERN', value='https://leetify.com/academy/csgo-spray-patterns#mp9', inline=False)
            await channel.send(embed=details)

        # MP5-SD
        elif name == 'MP5-SD' or name == 'mp5-sd':
            details = discord.Embed(
                title='Weapon: MP5-SD',
                description='Often imitated but never equaled, the iconic MP5 is perhaps the most versatile and ' +
                'popular SMG in the world. This SD variant comes equipped with an integrated silencer, making an already formidable weapon whisper-quiet.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/mp5-sd-0036a311f3dbe20a06aca7e1bff4450b.png')
            details.add_field(name='TYPE', value='SMG', inline=True)
            details.add_field(name='INGAME PRICE', value='$1500', inline=True)
            details.add_field(name='FIRE RATE',
                              value='750 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='CT/T(Common)', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='2.9 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='15 M', inline=True)
            details.add_field(name='MODE', value='Automatic', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$300/$600', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='30/120', inline=True)
            await channel.send(embed=details)

        # PP-BIZON
        elif name == 'PP-BIZON' or name == 'pp-bizon':
            details = discord.Embed(
                title='Weapon: PP-BIZON',
                description='The Bizon SMG is low-damage, but offers a uniquely designed high-capacity drum magazine that reloads quickly.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/pp-bizon-9eebce00c70ac8ebb58bc28a91002246.png')
            details.add_field(name='TYPE', value='SMG', inline=True)
            details.add_field(name='INGAME PRICE', value='$1400', inline=True)
            details.add_field(name='FIRE RATE',
                              value='750 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='CT/T(Common)', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='2.4 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='10 M', inline=True)
            details.add_field(name='MODE', value='Automatic', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$300/$600', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='64/120', inline=True)
            details.add_field(
                name='SPRAY PATTERN', value='https://leetify.com/academy/csgo-spray-patterns#bizon', inline=False)
            await channel.send(embed=details)

        # SAWED-OFF
        elif name == 'SAWED-OFF' or name == 'sawed-off':
            details = discord.Embed(
                title='Weapon: SAWED-OFF',
                description="The classic Sawed-Off deals very heavy close-range damage, but with its low accuracy, " +
                "high spread and slow rate of fire, you'd better kill what you hit.",
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/sawed-off-8ab74fc8ce3a65cc3eb8bdf632b35852.png')
            details.add_field(name='TYPE', value='Heavy', inline=True)
            details.add_field(name='INGAME PRICE', value='$1100', inline=True)
            details.add_field(name='FIRE RATE',
                              value='71 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='Terrorists', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='3.2 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE',
                              value='2.2 M', inline=True)
            details.add_field(name='MODE', value='Pump action', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$450/$900', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='7/32', inline=True)
            await channel.send(embed=details)

        # MAG-7
        elif name == 'MAG-7' or name == 'mag-7':
            details = discord.Embed(
                title='Weapon: MAG-7',
                description='The CT-exclusive Mag-7 delivers a devastating amount of damage at close range.' +
                'Its rapid magazine-style reloads make it a great tactical choice.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/mag-7-b7555abf69114ba233ba97bbccf3e09e.png')
            details.add_field(name='TYPE', value='Heavy', inline=True)
            details.add_field(name='INGAME PRICE', value='$1300', inline=True)
            details.add_field(name='FIRE RATE',
                              value='71 SHOTS/MIN', inline=True)
            details.add_field(
                name='SIDE', value='Counter-Terrorists', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='2.4 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE',
                              value='4.6 M', inline=True)
            details.add_field(name='MODE', value='Pump action', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$450/$900', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='5/32', inline=True)
            await channel.send(embed=details)

        # NOVA
        elif name == 'NOVA' or name == 'nova':
            details = discord.Embed(
                title='Weapon: NOVA',
                description="The Nova's rock-bottom price tag makes it a great ambush weapon for a cash-strapped team.",
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/nova-269bf37b093aa3fedac075036f238987.png')
            details.add_field(name='TYPE', value='Heavy', inline=True)
            details.add_field(name='INGAME PRICE', value='$1050', inline=True)
            details.add_field(name='FIRE RATE',
                              value='68 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='CT/T(Common)', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='3.7 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE',
                              value='3.2 M', inline=True)
            details.add_field(name='MODE', value='Pump action', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$450/$900', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='8/32', inline=True)
            await channel.send(embed=details)

        # XM1014
        elif name == 'XM1014' or name == 'xm1014':
            details = discord.Embed(
                title='Weapon: XM1014',
                description='The XM1014 is a powerful fully automatic shotgun that justifies its heftier ' +
                'price tag with the ability to paint a room with lead fast.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/xm1014-6fa544b8253221498d9879561cf0cc02.png')
            details.add_field(name='TYPE', value='Heavy', inline=True)
            details.add_field(name='INGAME PRICE', value='$2000', inline=True)
            details.add_field(name='FIRE RATE',
                              value='171 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='CT/T(Common)', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='2.8 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE',
                              value='3.4 M', inline=True)
            details.add_field(name='MODE', value='Automatic', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$450/$900', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='7/32', inline=True)
            await channel.send(embed=details)

        # NEGEV
        elif name == 'NEGEV' or name == 'negev':
            details = discord.Embed(
                title='Weapon: NEGEV',
                description='The Negev is a beast that can keep the enemy at bay with its pin-point supressive fire,' +
                ' provided you have the luxury of time to gain control over it.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/negev-2355f6c81f95c7f41bbe7b45dbe5960f.png')
            details.add_field(name='TYPE', value='Heavy', inline=True)
            details.add_field(name='INGAME PRICE', value='$1700', inline=True)
            details.add_field(name='FIRE RATE',
                              value='800 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='CT/T(Common)', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='5.7 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='13 M', inline=True)
            details.add_field(name='MODE', value='Automatic', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='150/300', inline=True)
            details.add_field(
                name='SPRAY PATTERN', value='https://leetify.com/academy/csgo-spray-patterns#negev', inline=False)
            await channel.send(embed=details)

        # M249
        elif name == 'M249' or name == 'm249':
            details = discord.Embed(
                title='Weapon: M249',
                description='A strong open-area LMG, the M249 is the perfect choice for players willing to ' +
                'trade a slow fire rate for increased accuracy and a high ammo capacity.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/m249-b8183ef1cf8fa2e57d0df817287bb911.png')
            details.add_field(name='TYPE', value='Heavy', inline=True)
            details.add_field(name='INGAME PRICE', value='$5200', inline=True)
            details.add_field(name='FIRE RATE',
                              value='750 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='CT/T(Common)', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='5.7 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='16 M', inline=True)
            details.add_field(name='MODE', value='Automatic', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='100/200', inline=True)
            details.add_field(
                name='SPRAY PATTERN', value='https://leetify.com/academy/csgo-spray-patterns#m249', inline=False)
            await channel.send(embed=details)

        # USP-S
        elif name == 'USP-S' or name == 'usp-s':
            details = discord.Embed(
                title='Weapon: USP-S',
                description='A fan favorite from Counter-Strike: Source, the Silenced USP Pistol has a ' +
                'detachable silencer that gives shots less recoil while suppressing attention-getting noise.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/usp-s-605aa989ed98c08df2cc3de4026b89fb.png')
            details.add_field(name='TYPE', value='Pistol', inline=True)
            details.add_field(name='INGAME PRICE', value='$200', inline=True)
            details.add_field(name='FIRE RATE',
                              value='352 SHOTS/MIN', inline=True)
            details.add_field(
                name='SIDE', value='Counter-Terrorists', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='2.2 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='21 M', inline=True)
            details.add_field(name='MODE', value='Semi-Auto', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='12/24', inline=True)
            await channel.send(embed=details)

        # GLOCK-18
        elif name == 'GLOCK-18' or name == 'glock-18':
            details = discord.Embed(
                title='Weapon: GLOCK-18',
                description='The Glock 18 is a serviceable first-round pistol that works best against ' +
                'unarmored opponents and is capable of firing three-round bursts.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/glock-18-cbacf12dbd4be93910ad9ebc54580111.png')
            details.add_field(name='TYPE', value='Pistol', inline=True)
            details.add_field(name='INGAME PRICE', value='$200', inline=True)
            details.add_field(name='FIRE RATE',
                              value='400 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='Terrorists', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='2.2 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='20 M', inline=True)
            details.add_field(
                name='MODE', value='Semi-Auto/Burst', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='20/120', inline=True)
            await channel.send(embed=details)

        # DESERT EAGLE
        elif name == 'DESERT EAGLE' or name == 'desert eagle':
            details = discord.Embed(
                title='Weapon: DESERT EAGLE',
                description='As expensive as it is powerful, the Desert Eagle is an iconic pistol that is ' +
                'difficult to master but surprisingly accurate at long range.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/desert-eagle-38cb46e2594ff557d231c663e85b53fd.png')
            details.add_field(name='TYPE', value='Pistol', inline=True)
            details.add_field(name='INGAME PRICE', value='$700', inline=True)
            details.add_field(name='FIRE RATE',
                              value='267 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='CT/T(Common)', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='2.2 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='25 M', inline=True)
            details.add_field(name='MODE', value='Semi-Auto', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='7/35', inline=True)
            await channel.send(embed=details)

        # P250
        elif name == 'P250' or name == 'p250':
            details = discord.Embed(
                title='Weapon: P250',
                description='A low-recoil firearm with a high rate of fire, the P250 is a relatively inexpensive choice against armored opponents.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/p250-e6a116b22759995e46b400f89b5522d3.png')
            details.add_field(name='TYPE', value='Pistol', inline=True)
            details.add_field(name='INGAME PRICE', value='$300', inline=True)
            details.add_field(name='FIRE RATE',
                              value='400 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='CT/T(Common)', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='2.2 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='21 M', inline=True)
            details.add_field(name='MODE', value='Semi-Auto', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='13/26', inline=True)
            await channel.send(embed=details)

        # FIVE-SEVEN
        elif name == 'FIVE-SEVEN' or name == 'five-seven':
            details = discord.Embed(
                title='Weapon: FIVE-SEVEN',
                description='Highly accurate and armor-piercing, the pricy Five-Seven is a slow-loader that ' +
                'compensates with a generous 20-round magazine and forgiving recoil.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/five-seven-e340fb7163184884f4314bd5ee2bbb2f.png')
            details.add_field(name='TYPE', value='Pistol', inline=True)
            details.add_field(name='INGAME PRICE', value='$500', inline=True)
            details.add_field(name='FIRE RATE',
                              value='400 SHOTS/MIN', inline=True)
            details.add_field(
                name='SIDE', value='Counter-Terrorists', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='2.2 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='14 M', inline=True)
            details.add_field(name='MODE', value='Semi-Auto', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='20/100', inline=True)
            await channel.send(embed=details)

        # CZ75-AUTO
        elif name == 'CZ75-AUTO' or name == 'cz75-auto':
            details = discord.Embed(
                title='Weapon: CZ75-AUTO',
                description='A fully automatic variant of the CZ75, the CZ75-Auto is another inexpensive choice ' +
                'against armored opponents. But with very little ammo provided, strong trigger discipline is required.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/cz75-auto-e677e16d69808bc7cf9425615933643c.png')
            details.add_field(name='TYPE', value='Pistol', inline=True)
            details.add_field(name='INGAME PRICE', value='$500', inline=True)
            details.add_field(name='FIRE RATE',
                              value='600 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='CT/T(Common)', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='2.7 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='11 M', inline=True)
            details.add_field(name='MODE', value='Automatic', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='12/12', inline=True)
            await channel.send(embed=details)

        # P2000
        elif name == 'P2000' or name == 'p2000':
            details = discord.Embed(
                title='Weapon: P2000',
                description='Accurate and controllable, the German-made P2000 is a serviceable first-round pistol that works best against unarmored opponents.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/p2000-c52f059472119553fd64922504701374.png')
            details.add_field(name='TYPE', value='Pistol', inline=True)
            details.add_field(name='INGAME PRICE', value='$200', inline=True)
            details.add_field(name='FIRE RATE',
                              value='352 SHOTS/MIN', inline=True)
            details.add_field(
                name='SIDE', value='Counter-Terrorists', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='2.2 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='22 M', inline=True)
            details.add_field(name='MODE', value='Semi-Auto', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='13/52', inline=True)
            await channel.send(embed=details)

        # TEC-9
        elif name == 'TEC-9' or name == 'tec-9':
            details = discord.Embed(
                title='Weapon: TEC-9',
                description='An ideal pistol for the Terrorist on the move, the Tec-9 is lethal in close quarters and features a high magazine capacity.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/usp-s-605aa989ed98c08df2cc3de4026b89fb.png')
            details.add_field(name='TYPE', value='Pistol', inline=True)
            details.add_field(name='INGAME PRICE', value='$500', inline=True)
            details.add_field(name='FIRE RATE',
                              value='500 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='Terrorists', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='2.5 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='13 M', inline=True)
            details.add_field(name='MODE', value='Semi-Auto', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='18/90', inline=True)
            await channel.send(embed=details)

        # R8 REVOLVER
        elif name == 'R8 REVOLVER' or name == 'r8 revolver':
            details = discord.Embed(
                title='Weapon: R8 REVOLVER',
                description='The R8 Revolver delivers a highly accurate and powerful round at the expense of a ' +
                'lengthy trigger-pull. Firing rapidly by fanning the hammer may be the best option when point-blank stopping power is required.',
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/r8-revolver-de180ed78875e37d2e1903cf9f6bbf6c.png')
            details.add_field(name='TYPE', value='Pistol', inline=True)
            details.add_field(name='INGAME PRICE', value='$600', inline=True)
            details.add_field(name='FIRE RATE',
                              value='600 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='CT/T(Common)', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='2.3 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='25 M', inline=True)
            details.add_field(name='MODE', value='Semi-Auto', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='8/8', inline=True)
            await channel.send(embed=details)

        # DUAL BERETTAS
        elif name == 'DUAL BERETTAS' or name == 'dual berettas':
            details = discord.Embed(
                title='Weapon: DUAL BERETTAS',
                description="Firing two large-mag Berettas at once will lower accuracy and increase load times." +
                " On the bright side, you'll get to fire two large-mag Berettas at once.",
                color=discord.Color.dark_red()
            )
            details.set_image(
                url='https://wiki.cs.money/_next/static/images/dual-berettas-1c945870e1ff70ef2b0915f20590c289.png')
            details.add_field(name='TYPE', value='Pistol', inline=True)
            details.add_field(name='INGAME PRICE', value='$400', inline=True)
            details.add_field(name='FIRE RATE',
                              value='500 SHOTS/MIN', inline=True)
            details.add_field(name='SIDE', value='CT/T(Common)', inline=True)
            details.add_field(name='RELOAD TIME',
                              value='3.8 Sec.', inline=True)
            details.add_field(name='ACCURACY RANGE', value='17 M', inline=True)
            details.add_field(name='MODE', value='Semi-Auto', inline=True)
            details.add_field(name='KILL AWARD',
                              value='$150/$300', inline=True)
            details.add_field(name='MAGAZINE CAPACITY',
                              value='30/120', inline=True)
            await channel.send(embed=details)

        else:
            await channel.send("Incorrect weapon name.")

    # WEAPON_ERROR HANDLER
    @weapon.error
    async def weapon_error(self, ctx, error):
        channel = self.client.get_channel(845246215796424704)
        if isinstance(error, commands.MissingRequiredArgument):
            await channel.send("Required weapon name.")

    # WEAPON LIST COMMAND
    @commands.command()
    async def list(self, ctx):
        channel = self.client.get_channel(845246215796424704)
        rifles = [
            'AK-47', 'AWP', 'M4A4', 'M4A1-S', 'AUG', 'SG 553',
            'GALIL AR', 'FAMAS', 'SSG 08', 'SCAR-20', 'G3SG1'
        ]

        heavy = [
            'P90', 'UMP-45', 'MAC-10', 'MP7',
            'MP9', 'MP5-SD', 'PP-BIZON', 'SAWED-OFF',
            'MAG-7', 'NOVA', 'XM1014', 'NEGEV', 'M249'
        ]

        pistol = [
            'USP-S', 'GLOCK-18', 'DESERT EAGLE',
            'P250', 'FIVE-SEVEN', 'CZ75-AUTO', 'P2000',
            'TEC-9', 'R8 REVOLVER', 'DUAL BERETTAS'
        ]

        rifleInfo = discord.Embed(
            title='RIFLES',
            description="List of all rifles!",
            color=discord.Color.dark_red()
        )
        for weapon in rifles:
            rifleInfo.add_field(name='*', value=weapon, inline=True)

        await channel.send(embed=rifleInfo)

        heavyInfo = discord.Embed(
            title='HEAVY',
            description="List of all heavy weapons!",
            color=discord.Color.dark_red()
        )
        for weapon in heavy:
            heavyInfo.add_field(name='*', value=weapon, inline=True)

        await channel.send(embed=heavyInfo)

        pistolInfo = discord.Embed(
            title='PISTOLS',
            description="List of all pistols!",
            color=discord.Color.dark_red()
        )
        for weapon in pistol:
            pistolInfo.add_field(name='*', value=weapon, inline=True)

        await channel.send(embed=pistolInfo)


def setup(client):
    client.add_cog(Weapon(client))
