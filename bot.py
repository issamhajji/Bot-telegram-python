# importa l'API de Telegram
from telegram.ext import Application, CommandHandler,ContextTypes
from telegram import Update
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://<userdb>:<password>@cluster0.v0nts.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

DB = client["mercadona_db"]
productes = DB.productes

# Definir estats
# CART = range(1)
cart = {}
# defineix una funció start que saluda i que s'executarà quan el bot rebi el missatge /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await update.message.reply_text(
        "👏 Benvingut\da"

    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """llistar comandes per a l'usuari"""
    await update.message.reply_text("No saps per on començar? Utilitza les comandes /start, /help, /info, /imatge, /compra")

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    codi = int(context.args[0])
    # resposta = "has demanat info sobre " + codi
    producte = productes.find_one({"id":codi})

    if producte:
        resposta = (
            f"***{producte.get('nom', 'N/D')}***\n"
            f"Codi: `{producte['id']}`\n\n"
            f"{producte['format']}\n\n"
            f"💲***{producte.get('preu', 'N/D')}***"
        )
        await update.message.reply_text(resposta, parse_mode="Markdown")  # Permet format Markdown
    else:
        await update.message.reply_text("⚠️ Producte no trobat.")

    # await update.message.reply_text(resposta)

async def imatge(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    codi = int(context.args[0])

    # resposta = "has demanat imatge sobre " + codi
    producte = productes.find_one({"id":codi})

    if producte:
        resposta = (
            f"***{producte.get('nom', 'N/D')}***\n"
            f"[.]({producte['url_imatge']})"
        )
        await update.message.reply_text(resposta, parse_mode="Markdown")  # Permet format Markdown
    else:
        await update.message.reply_text("⚠️ Producte no trobat.")

    # await update.message.reply_text(resposta)

async def compra(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    idusuari = update.message.from_user.id
    codi = int(context.args[0])
    quantitat = int(context.args[1])

    if idusuari not in cart:
        cart[idusuari] = {"total": 0}
    
    cart[idusuari]["total"] += quantitat
    resposta = f"has afegit la quantitat de {quantitat} unitats del producte {codi} a la cistella\n ara hi ha un total de {cart[idusuari]["total"]} productes a la cistella"
    await update.message.reply_text(resposta)

def main():
    # declara una constant amb el access token que llegeix de token.txt
    TOKEN = open('./token.txt').read().strip()
    print(TOKEN)
    
    application = Application.builder().token(TOKEN).build()
    #Definim les opcions que podrà executar
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("imatge", imatge))
    application.add_handler(CommandHandler("compra", compra))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()