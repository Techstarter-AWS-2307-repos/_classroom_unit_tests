import sys
import subprocess


def run_flake8():
    # führt flake8 aus und gibt die Anzahl der Probleme zurück
    result = subprocess.run(
        ["flake8", "../", "--count", "--exclude=unittests/"],
        stdout=subprocess.PIPE,
        text=True,
    )
    output = result.stdout.strip()

    try:
        error_count = int(output.strip().splitlines()[-1])
        print("Errors:", error_count)
    except ValueError:  # Nicht-numerische Ausgabe bedeutet 0 Fehler
        error_count = 0
    return error_count


def calculate_grade(max_points, error_count, points_per_error):
    # Zieht Punkte für jeden Flake8-Fehler ab
    points_lost = min(error_count * points_per_error, max_points)
    grade = max_points - points_lost
    return grade


def main():
    max_points = 100  # Maximale Punktzahl für die Aufgabe
    points_per_error = 1  # Punkte, die pro Fehler abgezogen werden

    error_count = run_flake8()
    grade = calculate_grade(max_points, error_count, points_per_error)

    print(f"Flake8 Fehler: {error_count}")
    print(f"Endnote: {grade}/100")

    # Wenn die Note niedriger als der Maximalwert ist, Exitcode auf 1 setzen
    if grade < max_points:
        sys.exit(0)


if __name__ == "__main__":
    main()
