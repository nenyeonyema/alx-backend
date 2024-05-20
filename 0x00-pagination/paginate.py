def paginate_simple(data, page, page_size):
    if page < 1 or page_size < 1:
        return []
    offset = (page - 1) * page_size
    return data[offset:offset + page_size]

# Example dataset with 100 items
data = [f"Item {i}" for i in range(1, 101)]

# Fetch page 1 with 10 items per page
page = 1
page_size = 10
result = paginate_simple(data, page, page_size)
print(f"Page {page}:", result)

# Fetch page 2 with 10 items per page
page = 2
result = paginate_simple(data, page, page_size)
print(f"Page {page}:", result)

# Fetch page 3 with 10 items per page
page = 3
result = paginate_simple(data, page, page_size)
print(f"Page {page}:", result)
