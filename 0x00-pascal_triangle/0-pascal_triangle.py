def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        for j in range(1, i):
            # Calculate the middle elements based on the previous row
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle

# Example usage
if __name__ == "__main__":
    triangle_result = pascal_triangle(5)
    for row in triangle_result:
        print(row)

