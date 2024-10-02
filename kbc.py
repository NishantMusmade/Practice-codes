#kbc using list

questions = [
    "What is the capital of France?",
    "Who wrote 'To Kill a Mockingbird'?",
    "What is the chemical symbol for gold?",
    "What is the square root of 64?",
    "Who painted the Mona Lisa?",
    "What is the largest planet in our solar system?",
    "In which year did World War II end?",
    "What is the powerhouse of the cell?",
    "Who discovered penicillin?",
    "What is the chemical formula for water?"
]

options = [
    ["Paris", "London", "Berlin", "Rome"],  # Options for question 1
    ["Harper Lee", "J.K. Rowling", "Stephen King", "George Orwell"],  # Options for question 2
    ["Au", "Ag", "Fe", "Au"],  # Options for question 3
    ["4", "6", "8", "10"],  # Options for question 4
    ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Michelangelo"],  # Options for question 5
    ["Jupiter", "Saturn", "Mars", "Venus"],  # Options for question 6
    ["1945", "1939", "1950", "1940"],  # Options for question 7
    ["Mitochondria", "Nucleus", "Ribosome", "Chloroplast"],  # Options for question 8
    ["Alexander Fleming", "Marie Curie", "Louis Pasteur", "Albert Einstein"],  # Options for question 9
    ["H2O", "CO2", "NaCl", "NH3"]  # Options for question 10
]

correct_answers = ["Paris", "Harper Lee", "Au", "8", "Leonardo da Vinci", "Jupiter", "1945", "Mitochondria", "Alexander Fleming", "H2O"]

prize_money = [10000,20000,40000,80000,160000,320000,640000,1280000,2450000,5000000]

sum=0

for question,option,correct,money in zip(questions,options,correct_answers,prize_money):
    print("\n"+ question)
    print("\n1. ",option[0],"\t\t2. ",option[1])
    print("3. ",option[2],"\t\t4. ",option[3])
    choice = int(input("Enter your choice: "))
    if (option[choice-1]==correct):
        sum = sum + money
        print("It's a correct answer")
        print("Current winnings: ",sum)
    else:
        print("Oops!!!Wrong Answer")
        break

if sum == 10000000:
    print("\nCongratulations, You have won 1 crore")
else:
    print("\nYou have won total Rs.",sum)
