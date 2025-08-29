# Write a Python program that manages a list of student scores. Perform the following operations step-by-step:
# Create an empty list to store scores.
# Append the scores: 85, 90, 78, 92, 88
# Insert the score 80 at index 5
# Remove the score 92 from the list
# Sort the scores in ascending order
# Reverse the list
# Find and print the maximum and minimum score
# Check if 90 is in the list
# Print the total number of scores
# Slice and print the first three scores
# find the last element from the list
# replace the score with new score on the index 2
# create a new copied list also

scores = []  # Create an empty list to store scores
scores.extend([85, 90, 78, 92, 88])  # Append scores

print("Scores after appending:", scores)

scores.insert(5, 80)  # Insert score 80 at index 5
print("Scores after insert:", scores)

scores.remove(92)  # Remove score 92 from the list
print("Scores after removal of 92:", scores)

scores.sort() # Sorting the list
print("Scores after sort:", scores)

scores.reverse()  # Reverse the list
print("Scores after reverse:", scores)

print("Max:", max(scores))  #max

print("Min:", min(scores))  #min

print("Check if 90 is there?", 90 in scores)  # Check if it is there


total = sum(scores) # Sum of scores
print("Total number of scores:", total) # Total number of scores

first_three = scores[:3]  # Slice first three scores
print("First three scores:", first_three)

last_element = scores[-1]  # Last element
print("Last element:", last_element)

scores[2] = 55  # Replace score at index 2
print("Scores after replacing index 2 with 55: ", scores)    

copied_score = scores.copy()  # Create a copied list
print("Copied list of scores:", copied_score)

print("Copied list of scores:", copied_score)

#loop over the list scores to greatete a switch case to print the grade for each score  
print("Looping over the scores list:")  
for score in scores:
    match score:
        case num if num > 90:
            grade = 'A'
            print("Your grade from switch is: A")
        case num if num > 80:
            grade = 'B'
            print("Your grade from switch is: B")        
        case num if num > 70:
            grade = 'C'
            print("Your grade from switch is: C")
        case num if num > 60:
            grade = 'D'
            print("Your grade from switch is: D")
        case _:  # default case
            grade = 'F' 
            print("Your grade from switch is: F")




