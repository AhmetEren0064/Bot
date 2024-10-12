import discord, random, os, requests
from discord.ext import commands

cevreci_kuruluslar = {
    1: "GP: Bu grup, çevre kirliliğine karşı savaş açmış, doğayı koruma peşinde koşan bir ekip. Kısacası, 'doğa benim dostum' diyenlerin takımı. Okyanusları temizler, ağaçları korur, kötü enerji kaynaklarıyla savaşır.",
    2: "WWF: Hayvanların ve doğanın dostu olan bu ekip, dünya üzerindeki biyoçeşitliliği korumaya ant içmiş. Ormanları, denizleri korur; tehdit altındaki türler için savaşır.",
    3: "TNC: Doğanın koruyucusu. Ekosistemleri korumak için her yere el atan bir ekip. Ağaç diker, su kaynaklarını korur, doğal alanları kurtarır.",
    4: "FoE: Doğanın adaletini savunan bir grup. 'Bizi kirletme!' diyenlerin ekibi. Çevre adaletini sağlamak için mücadele eder, yerel sorunlara dikkat çeker.",
    5: "SC: ABD’nin en eski çevre grubu. Fosil yakıtlarla savaşır, doğal alanları korur. 'Sierra biziz!' diyenlerin grubu.",
    6: "350.org: İklim değişikliğiyle mücadele eden bir topluluk. Karbonu düşürüp gezegeni kurtarma peşindeler. Fosil yakıtları protesto ederler, yenilenebilir enerji desteklerler.",
    7: "EJ: Doğanın avukatları. Çevre yasalarının koruyucusu. Çevre yasalarını mahkemelerde savunur, doğanın haklarını korur.",
    8: "RA: Ormanları kurtarma peşindeki bir grup. 'Ağaç dostu, çevre dostu!' diyenlerin takımı. Sürdürülebilir tarımı teşvik eder, biyoçeşitliliği korur.",
    9: "PPC: Plastik kirliliğiyle savaş açan ekip. 'Plastikler gitsin!' diyorlar. Tek kullanımlık plastiklere karşı mücadele eder, farkındalık yaratırlar.",
    10: "OC: Okyanusların dostları. Denizlerimizi koruma peşindeler. Okyanusları temizler, deniz canlılarını korur.",
    11: "C40: İklim değişikliğiyle savaşan şehirlerin ittifakı. Şehirlerin karbon emisyonlarını düşürmek için çalışır.",
    12: "YCC: Gençlerin sesi, iklim aktivistleri. 'Biz geleceğiz!' diyerek iklim için savaşırlar. Gençleri bilinçlendirip etkinlikler düzenlerler.",
    13: "EDN: Dünya Günü'nü organize eden ekip. Çevre için farkındalık yaratıp etkinlikler düzenler.",
    14: "GA: Sürdürülebilir yaşamı destekleyen bir grup. Çevre dostu iş modellerini destekler, yeşil yaşamı teşvik eder.",
    15: "WCS: Yaban hayatın koruyucusu. Tehdit altındaki türlerin korunmasına odaklanır.",
    16: "NatureServe: Biyoçeşitliliği takip eden grup. Koruma verilerini sağlar ve türlerin durumunu izler.",
    17: "CI: Dünya genelinde doğayı korumaya çalışan bir grup. Ekosistemlerin korunması için çalışır.",
    18: "CBC: Biyoçeşitliliğin korunması için çalışan bir ekip. Koruma projeleri geliştirir ve türleri araştırır.",
    19: "NGS: Keşif ve koruma için çalışan bir ekip. Doğal alanları belgeleyip projeleri destekler.",
    20: "FoEE: Avrupa'da çevre adaletini savunan bir grup. Çevresel adaleti sağlar ve yerel toplulukları destekler.",
    21: "Wildlife Trusts: Yaban hayvanlarını ve doğal alanları koruma peşinde koşan bir grup.",
    22: "EDF: Çevre yasalarını destekleyen bir grup. Çevresel adaleti ve politika oluşumunu desteklerler.",
    23: "POW: Kış sporları severler için iklim değişikliğine karşı savaşan bir grup.",
    24: "IUCN: Uluslararası doğa koruma organizasyonu. Türlerin korunması için stratejiler geliştirir.",
    25: "Biodiversity Int.: Biyoçeşitliliği koruma odaklı çalışan bir grup. Tarım ve türlerin korunmasına yönelik çalışmalar yürütürler.",
    26: "IIED: Çevresel ve sosyal adaleti savunan bir ekip. Sürdürülebilir gelecek için projeler yürütürler.",
    27: "Earth Guardians: Genç aktivistlerden oluşan bir grup. Gençleri iklim hareketine dahil ederler.",
    28: "Oxfam: Yoksulluk ve eşitsizlikle savaşan bir organizasyon. Çevresel adaleti desteklerler.",
    29: "Global Green: Çevre dostu projeleri destekleyen bir grup. Sürdürülebilir girişimlere yatırım yapar.",
    30: "No More Plastic: Plastik kirliliğiyle savaş açmış bir grup. Tek kullanımlık plastikleri azaltmak için çalışırlar."
}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def stk(ctx):
    a = random.randint(0,30)
    await ctx.send(cevreci_kuruluslar[a])

@bot.command()
async def help(ctx):
    await ctx.send("$stk komutunu yazarsan sana herhangi bir doğa koruma amacına sahip sivil toplum kuruluşu söylerim!")

bot.run("TOKEN")
