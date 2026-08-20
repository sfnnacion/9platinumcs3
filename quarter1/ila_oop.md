# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation can be used in the sari-sari store inventory by letting us group all the information about a specific product (like its name, price, and how many pieces are in stock) inside one class called Product. Instead of letting any part of the program change these values directly, we can keep the data safe inside the class and use methods like sellItem() or restock() to be able to update them. This helps improve our code design as it stops bugs like having no more or negative stock count, which makes our inventory tracker much more organized and reliable.

### 2. Abstraction
Abstraction helps simplify how we interact with the inventory by hiding the complicated code happening in the background. An example is when the tindero/tindera wants to sell an item, they just need to call a simple method like checkout(), without needing to worry about the messy code calculating the total. This keeps our system user-friendly and makes it way easier to read and maintain.

### 3. Inheritance
With inheritance, we don't need to rewrite the same properties over and over again for different kinds of items in the store. We can make a general Product class with the basic traits (like name and price), then make subsclasses for items with expiration dates. These subclasses automatically get all the features of a normal product while letting us add unique details, which helps with keeping our project structure clean and organized.

### 4. Polymorphism
Polymorphism lets us use the same method name for different type of products. For example, both regular store items and special items can have a compute_discount() method, but each class can compute the prices differently. This makes the overall design flexible because our main program can loop through a mixed list of inventory items and call the exact same method without needing to check what specific kind of product it is first.

## Reflection
Among the four pillars of the Object-Oriented Programming (OOP), I think that encapsulation is the most useful fpr improving the inventory system of the sari-sari store because keeping data secure is super important when dealing with the object's price and their stocks. If we didn't use encapsulation, it would be easy to have accidentally mess up the inventory. By combining the data with specific methods, we can ensure that every transaction is handled correctly every time.