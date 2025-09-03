def reverse_string(text):
    return text[::-1]
def count_word(text):
    words=text.split()
    return len(words)
print("FLOW CONTROL,FUNCTIONS AND STRING MANIPULATIONS")
input_text=input("Enter a sentence:")
if input_text.startswith("Hello"):
    print("Greeting:Hello!")
elif input_text.startswith("Good bye"):
    print("parting:Goodbye!")
else:
    print("custom message:",input_text)
reversed_text=reverse_string(input_text)
print("Reversed text:",reversed_text)
word_count=count_word(input_text)
print("word count:",word_count)
