#ობიექტი არის მონაცემთა სტრუქტურა
#dictionary გამოიყენება პითონში მონაცემთა ორგანიზებაში
mouse = {
    "brand": "Logitech",
    "model": "3",
    "dpi": 4000,
    "buttons": 7,
    "wireless": True
}
mouse_keys = mouse.keys() 
print(mouse_keys) 
mouse_values = mouse.values() 
print(mouse_values) 
mouse_items = mouse.items() 
print(mouse_items)

computer = {
    "brand": "lenovo",
    "model": "thinkpad",
    "processor": "i7",
    "ram": "16GB",
    "storage": "1TB SSD"
}
computer_keys = computer.keys() 
print(computer_keys) 
computer_values = computer.values() 
print(computer_values) 
computer_items = computer.items() 
print(computer_items)

keyboard = {
    "brand": "genius",
    "model": "2",
    "switch_type": "Mechanical",
    "backlit": True,
    "connection": "USB"
}
keyboard_keys = keyboard.keys() 
print(keyboard_keys) 
keyboard_values = keyboard.values() 
print(keyboard_values) 
keyboard_items = keyboard.items() 
print(keyboard_items)