import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Lista di nomi da cui scegliere casualmente
NOMI = []

# Dizionario per salvare i nomi degli utenti
utenti = {}

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    messaggio_di_inizio = (
        "🎅 Benvenuto al bot del Babbo Natale Segreto! 🎄\n\n"
        "Ecco come funziona:\n"
        "1️⃣ Scrivi il tuo nome in chat. Questo ci permette di inserirti nel gioco e fare in modo che tu non sia assegnato a te stesso.\n"
        "2️⃣ Usa il comando /ilmiobabbosegreto per scoprire chi sarà il tuo Babbo Natale segreto!\n\n"
        "❗ Nota: Ogni persona inserita nella lista sarà esclusa dall'essere il proprio Babbo Natale.\n\n"
        "✨ Inizia scrivendo il tuo nome per partecipare! ✨"
    )
    await update.message.reply_text(messaggio_di_inizio)


# Gestisce i messaggi di testo per salvare il nome dell'utente
async def salva_nome(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    nome_utente = update.message.text
    user_id = update.message.from_user.id

    # Salva il nome dell'utente nel dizionario
    utenti[user_id] = nome_utente
    print(utenti)
    await update.message.reply_text(f"Grazie, {nome_utente}! Scrivi il comando /ilmiobabbosegreto per scoprire il tuo babbo segreto.")
    NOMI.append(nome_utente)

# Comando /nomecasuale
async def nome_casuale(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id

    # Verifica se l'utente ha già inserito il suo nome
    if user_id not in utenti:
        await update.message.reply_text("Prima dimmi il tuo nome!")
        return

    # Nome dell'utente
    nome_utente = utenti[user_id]


    # Filtra la lista per evitare il nome dell'utente
    nomi_disponibili = [nome for nome in NOMI if nome.lower() != nome_utente.lower()]

    # Se ci sono nomi disponibili, scegliene uno casualmente
    if nomi_disponibili:
        nome_scelto = random.choice(nomi_disponibili)
        await update.message.reply_text(f"Il tuo babbo segreto è: {nome_scelto}")
    else:
        await update.message.reply_text("Ops! Non ci sono altri nomi disponibili nella lista.")

# Main del bot
def main():
    # Inserisci il TOKEN fornito da BotFather
    TOKEN = "7881435233:AAGK32twbrEvZ7bEWnaiPGKjgONHrbb33E0"

    # Crea l'applicazione del bot
    app = ApplicationBuilder().token(TOKEN).build()

    # Aggiungi i gestori di comandi e messaggi
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ilmiobabbosegreto", nome_casuale))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, salva_nome))

    # Avvia il bot
    print("Bot in esecuzione...")
    
    app.run_polling()

if __name__ == "__main__":
    main()
