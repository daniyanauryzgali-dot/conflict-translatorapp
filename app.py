import streamlit as st
from groq import Groq

st.title("Conflict Translator 2.0")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

text = st.text_area("Введите фразу для разбора:")
style = st.selectbox("Стиль ответа:", ["Дружелюбный", "Профессиональный", "Нейтральный"])

if st.button("Анализировать"):
    if text:
        my_prompt = f"""
        Проанализируй кратко: "{text}"
        1. Какие здесь эмоции? Напиши "здесь проявляется эмоция:  " и опиши эмоцию парой слов.
        2. Какие есть риски для отношений, если ответить агрессивно?
        3. Как лучше изменить эту фразу? Измени мою фразу, чтобы она не была агрессивной.
        4. Пример ответа в стиле {style}:
        """
        
        try:
            chat = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": my_prompt}]
            )
            
            st.markdown("---")
            st.markdown("### Результат разбора:")
            st.write(chat.choices[0].message.content)
            
        except Exception as e:
            st.error(f"Технический сбой: {e}")
    else:
        st.warning("Сначала введите текст!")
