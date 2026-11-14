score = 100
if score >= 90:
    print("Grade: A")
elif score >= 80 and score < 90: 
    print("Grade B")
else:
    print("Grade: F")

"A" if score >= 90 else "B" if score >= 80 and score < 90 else "F"
# inline if statement

# if condition 1:
#     do A

# else:
#     do B

# inline: do A if condition 1 else do B

"A" if score >= 90 else "F"

# CASE

country = "India"
match country:
    case "United States" | "USA" | "US":
        print("US")
    case "India":
        print("IN")
    case "Japan":
        print("JP")
    case "United Kingdom" | "UK":
        print("UK")