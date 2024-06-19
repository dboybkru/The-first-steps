import openai

def chat_with_neural_network():
    # Создаем клиента OpenAI
    client = openai.OpenAI(
        api_key="sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I",
        base_url="https://api.proxyapi.ru/openai/v1",
    )

    print("Начать чат с нейросетью. Введите 'exit' для выхода.")
    conversation = [{"role": "user", "content": "Hello, world"}]  # Начальное сообщение

    while True:
        user_input = input("Вы: ")
        if user_input.lower() == 'exit':
            break

        conversation.append({"role": "user", "content": user_input})        
        # conversation = [{"role": "system", "content": "Hello world"}] 

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=conversation
            )

            response_message = response.choices[0].message.content
            print(f"Нейросеть: {response_message}")

            # Добавляем ответ нейросети в историю общения
            conversation.append({"role": "assistant", "content": response_message})
            
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    chat_with_neural_network()