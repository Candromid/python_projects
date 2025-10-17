def validate_data(data):
    valid_extensions = {'txt', 'docx'}  # допустимые расширения файлов

    def valid_ip(ip):
        parts = ip.split(".")
        return len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)

    def valid_files(files):
        all_files = " ".join(files).split()
        return all(any(fname.endswith(f".{ext}") for ext in valid_extensions) for fname in all_files)

    # фильтруем данные сразу в одну строку
    return [record for record in data if valid_ip(record[0]) and valid_files(record[1])]


# тестовые данные
data = [
    ["128.16.35.a4", ["file_21.txt @data_report.txt notes2024.txt"]],
    ["34.56.42,5", ["file.txt analysis_results.ttx notes2000.txt"]],
    ["128.0.0.255", ["file_1.txt document_2024.docx notes2022.txt"]],
    ["240.127.56.340", ["file_432.txt ^budget_summary.txt notes2021.txt"]],
    ["192.168.1.10", ["file_432.txt important_info.txt notes1900.txt"]],
    ["192.c8.1.10", ["file_432.xt &meeting_notes.docx notes1995.txt"]],
    ["10.20.30.40", ["file_432.txt analysis_results.txt notes1998.txt"]],
]

# фильтруем
filtered_data = validate_data(data)

# вывод результата
print("Корректные записи:")
for item in filtered_data:
    print(item)
