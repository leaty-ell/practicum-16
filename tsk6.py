def decrypt_equation() -> None:
    """
    Decrypts the equation HOD+HOD+HOD=MAT.
    """
    solutions = []
    for hod in range(100, 1000):
        hod_str = str(hod)
        mat = hod * 3
        
        if mat < 100 or mat > 999:
            continue
        
        mat_str = str(mat)
        all_digits = hod_str + mat_str 
        
        if len(set(all_digits)) == 6: 
            solutions.append(hod)
    
    solutions.sort()
    for hod in solutions:
        print(f"{hod}+{hod}+{hod}={hod*3}")

def main():
    decrypt_equation()

if __name__ == "__main__":
    main()
