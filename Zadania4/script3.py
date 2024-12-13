from collections import OrderedDict

test_dict = {5: "Hum", 7: "HumHum", 1: "HumHumHUm"}

test_ordered_dict = OrderedDict()
for key, value in test_dict.items():
    test_ordered_dict[key] = value

test_dict[7] = "Pop"
test_ordered_dict[7] = "Pop"

print(test_dict)
print(test_ordered_dict)