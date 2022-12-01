# Open input file and read each line as a list
with open("221201_Code_Puzzles/day_01/day_01_input.txt") as f:
    items = [item.rstrip() for item in f]

elf_info_list = []
elf_id = 0
elf_calories = 0
for item in items:
    if item == "":
        elf_info_list.append(elf_calories)
        elf_calories = 0
        elf_id += 1
    else:
        elf_calories += int(item)

# Get max elf_id
# max_elf = max(zip(elf_info.values(), elf_info.keys()))[1]
# print(f"Max elf id: {max_elf}\nCalories: {elf_info[max_elf]}")

# Sort list of calories
elf_info_list.sort(reverse=True)

# Part 1 Get max calories
max_elf_calories = elf_info_list[0]

print(f"Max Calorie Elf: \n{max_elf_calories}\n")

# Part 2 Sum top 3 elf calories
top_three_sum = sum(elf_info_list[:3])

print(f"Top 3 Elf Calories: \n{top_three_sum}")
