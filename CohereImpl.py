
import cohere

api_key = "fEm4wDFUGpL6X8YFwbnXpfT5poFmfEVH3DBcNN59"  #My API key  
client = cohere.Client(api_key)


conversation_history = []        # This is a list to  store the conversation history

def poser_question(question):
    global conversation_history  # we use the same history for all calls

    
    conversation_history.append({"role": "USER", "message": question})      # To add the user's message to the history

    # Send request to Cohere with the full history
    response = client.chat(
        model="command-xlarge-nightly",
        message=question,
        chat_history=conversation_history  # this keeps track of the context
    )

    conversation_history.append({"role": "CHATBOT", "message": response.text})     # Add the bot's reply to the history

    return response.text


if __name__ == "__main__":
    print("Salut ! Je suis prêt à discuter, comment puis-je vous aider ? Tapez 'quit' pour arrêter.\n")

    while True:
        question = input("Vous: ")
        if question.lower() in ["quit", "exit", "stop"]:
            print("Au revoir, à bientôt !")
            break

        reponse = poser_question(question)
        print("Bot:", reponse)

