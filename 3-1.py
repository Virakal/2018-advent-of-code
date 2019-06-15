from claim import Claim

with open('3.txt', 'r') as f:
    lines = list(f)

# Debug
# lines = [
#     "#1 @ 1,3: 4x4",
#     "#2 @ 3,1: 4x4",
#     "#3 @ 5,5: 2x2",
# ]

claims = []

for line in lines:
    claim = Claim.from_string(line)
    claims += claim.get_claimed_coords()

claimed_coords = {}

for coords in claims:
    if coords in claimed_coords:
        claimed_coords[coords] += 1
    else:
        claimed_coords[coords] = 1

disputed_coords = [coords for coords, num in claimed_coords.items() if num > 1]

print(len(disputed_coords))
