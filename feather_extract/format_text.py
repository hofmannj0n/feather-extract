def format_extracted_text(extracted_text):
    formatted = list(extracted_text.split())
    formatted = formatted[7:]
    headers = formatted[0:4]
    headers = [headers[0], headers[1], ' '.join(headers[2:])]
    data = formatted[4:]
    formatted_data = []
    i = 0
    while i < len(data):
        item_start = i
        item_end = i + 1
        while item_end < len(data) and not data[item_end].isdigit():
            item_end += 1
        item = " ".join(data[item_start:item_end])
        
        if item_end < len(data):
            quantity = data[item_end]
            i = item_end + 1
        else:
            break

        bar_designation_start = i
        bar_designation_end = bar_designation_start + 2
        if len(data) > bar_designation_end:
            bar_designation = " ".join(data[bar_designation_start:bar_designation_end])
            i = bar_designation_end
        else:
            bar_designation = " ".join(data[bar_designation_start:])
            i = len(data)
        
        formatted_data.append([item, quantity, bar_designation])
    
    return formatted_data