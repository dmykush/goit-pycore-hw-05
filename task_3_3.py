import sys
from collections import Counter

def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)
    if len(parts) < 4:
        return None
    date, time, level, message = parts
    return {'date': date, 'time': time, 'level': level, 'message': message.strip()}

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    return list(filter(lambda log: log['level'] == level, logs))

def count_logs_by_level(logs: list) -> dict:
    levels = [log['level'] for log in logs]
    return dict(Counter(levels))

def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<17} | {'Кількість':<8}")
    print('-' * 17 + '-|-' + '-' * 8)
    for level in ['INFO', 'DEBUG', 'ERROR', 'WARNING']:
        print(f"{level:<17} | {counts.get(level, 0):<8}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Вкажіть шлях до лог-файлу.")
        sys.exit(1)
    file_path = sys.argv[1]
    filter_level = sys.argv[2] if len(sys.argv) > 2 else None
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)
    if filter_level:
        filtered_logs = filter_logs_by_level(logs, filter_level)
        print(f"\nДеталі логів для рівня '{filter_level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
