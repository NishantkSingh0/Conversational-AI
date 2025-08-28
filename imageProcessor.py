Describe = {
    'img095383': 'A bowl of dal makhni. The user is showcasing a spoonful of dal makhni. There is a large, thick iron nail visible nearby.',
    'img095052': 'A simple corn pizza slice. The user is pulling a plastic-like string that is stuck between the pizza layers.',
    'img095323': 'A large cheese burst pizza. All the cheese and pizza base have slid to the right side of the box. The cheese is overflowing at the top-right corner, and the slices are completely mixed together messily.',
    'img095532': 'A creamy momos box. All the cream and momos have shifted to the left side of the box. Some cream has spilled onto the floor. The box is in poor condition and is fully expanded on the left side.',
    'img095715': 'A large cheese burst pizza. All the cheese and pizza base have slid to the left side of the box. The cheese is overflowing at the top-left corner, and the slices are mixed together messily.',
    'img095840': 'A transparent polythene bag containing a dal makhni box. The curry has spilled over the polythene, and the box lid is broken.',
    'img100006': 'A top view of a white polythene containing a dal makhni box. The curry has spilled over the polythene, and the box lid is broken.'
}

def process(image_id):
    try:
        return Describe[image_id]
    except KeyError:
        return 'The image is not recognizable'