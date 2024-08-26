import keyboard

target_letter = 'q'  # Specify the letter that will stop the loop

print(f"Press '{target_letter}' to stop the loop...")

while True:
    # Your loop logic goes here
    print("Running...")

    # Break the loop if the target letter is pressed
    if keyboard.is_pressed(target_letter):
        print(f"'{target_letter}' pressed, stopping the loop.")
        break
q