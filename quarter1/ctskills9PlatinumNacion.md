## Annex A

## Computational Thinking Exercise: "Smart School Canteen Queue"
Section: 9 - Platinum                                                   Score:
C# / Name: Stacey Fame N. Nacion                                        Date: 08/15/26


Scenario
The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:
- Some students take too long to decide what to order.
- The cashier has to manually calculate totals and give change.
- There is no system to track which food items are running out.
Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.


Step 1: Identify the Big Problem
Main Problem: 
The school canteen gets too crowded and slow during lunch break because the ordering process is manual, students take time choosing, and there is no system to check available food or calculate totals quickly.

Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:
1. Slow decision making: Students spend too much time thinking about what to buy right when they reach the front of the line because they haven't seen a clear menu beforehand.
2. Manual Payment and Calculation: The cashier has to compute prices and count change by hand, which takes up a lot of time and can sometimes lead to calculation mistakes.
3. No Inventory Tracking: The canteen staff doesn't know when food items are running low or out of stock.


Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills: 

Sub-Problem #1: Slow Decision Making
   CT Skill: Abstraction
   Example Solution: Put up a large printed menu board outside the queue line shwoing only important details (like the food name and its price) so students can already decide what to buy while waiting in line

Sub-Problem #2: Manual Payment and Calculation
   CT Skill: Algorithm Design
   Example Solution: Make a simple calculator program where the cashier just types in the item prices, and the computer automatically computes the total and the exact change.

Sub Problem #3: No Inventory Tracking
   CT Skill: Decomposition
   Example Solution: Break down the inventory into a list where every time an item is sold, the system automatically subtracts one from the total stock count. 


Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem
Pseudocode for Sub-Problem #2: Manual Payment & Calculation

START
    total = 0

    // Add item prices
    PRINT "Enter price (0 to finish): "
    INPUT price
    
    WHILE price > 0
        total = total + price
        PRINT "Enter price (0 to finish): "
        INPUT price
    END WHILE

    PRINT "Total: ", total

    // Get the payment
    REPEAT
        PRINT "Enter cash given: "
        INPUT cash
        IF cash < total THEN
            PRINT "Not enough money."
        END IF
    UNTIL cash >= total

    // Give the change
    change = cash - total
    PRINT "Change: ", change
END


Reflection/Explanation:
Breaking down the big canteen problem into smaller parts made it much easier to understand. Using the computational thinking skills helped me create logical and realistic fixes to the problem. It saves a lot of time and prevents mistakes for both the students and cashier instead of when doing it manually.
