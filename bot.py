import os
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

verdades = [
    "¿Cuál es tu mayor secreto?",
    "¿Quién te gusta actualmente?",
    "¿Qué es lo más vergonzoso que te ha pasado?"
]

retos = [
    "Envía un emoji extraño.",
    "Cambia tu foto de perfil por 10 minutos.",
    "Escribe un mensaje divertido en el grupo."
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 ¡Hola! Soy tu bot de diversión.\n\nComandos:\n/verdad\n/reto"
    )

async def verdad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎲 VERDAD:\n" + random.choice(verdades)
    )

async def reto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 RETO:\n" + random.choice(retos)
    )

def main():
    token = os.getenv("BOT_TOKEN")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("verdad", verdad))
    app.add_handler(CommandHandler("reto", reto))

    app.run_polling()

if __name__ == "__main__":
    main()
