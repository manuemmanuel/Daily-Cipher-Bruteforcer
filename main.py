import pyautogui
import time

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'
}

def input_morse(sequence):
    for char in sequence:
        for signal in morse_code[char]:
            if signal == '.':
                pyautogui.click()  
            elif signal == '-':
                pyautogui.mouseDown() 
                time.sleep(0.5)
                pyautogui.mouseUp()
            time.sleep(0.2) 
        time.sleep(1) 
    time.sleep(1) 

def generate_alphabet_combinations():
    return list(morse_code.keys())

# Main brute-force function
def brute_force_morse():
    correct_sequence = []
    possible_letters = generate_alphabet_combinations()
    
    while True:
        current_sequence = ''.join(correct_sequence)
        for letter in possible_letters:
            for correct_letter in correct_sequence:
                input_morse(correct_letter)
                time.sleep(1) 
            
            input_morse(letter)
            time.sleep(1)  

        user_input = input(f"Which letter was correct for position {len(correct_sequence) + 1}? (Enter the letter or 'exit' to stop): ").strip().upper()
        if user_input in morse_code:
            correct_sequence.append(user_input)
        elif user_input == 'EXIT':
            print("Exiting.")
            break
        else:
            print("Invalid input. Exiting.")
            break

    print("Correct sequence:", ''.join(correct_sequence))

brute_force_morse()
