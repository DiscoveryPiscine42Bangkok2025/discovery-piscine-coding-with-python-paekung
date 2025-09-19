#!/usr/bin/env python3

def checkmate(board: str):
    try:
        g = [list(r) for r in board.splitlines() if r]
        n = len(g)
        if n == 0 or any(len(r) != n for r in g):
            print("Fail")
            return

        # หา King
        kings = [(i, j) for i in range(n) for j in range(n) if g[i][j] == 'K']
        if len(kings) != 1:
            print("Fail")
            return
        kr, kc = kings[0]

        def ray(dr, dc, attackers):
            r, c = kr + dr, kc + dc
            while 0 <= r < n and 0 <= c < n:
                v = g[r][c]
                if v != '.':
                    return v in attackers
                r += dr
                c += dc
            return False

        # Pawn โจมตีเฉียงลง
        if any(
            0 <= r < n and 0 <= c < n and g[r][c] == 'P'
            for r, c in [(kr + 1, kc - 1), (kr + 1, kc + 1)]
        ):
            print("Success")
            return

        # Rook หรือ Queen ตามแนวตรง
        if any(ray(dr, dc, {'R', 'Q'}) for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]):
            print("Success")
            return

        # Bishop หรือ Queen ตามแนวทแยง
        if any(ray(dr, dc, {'B', 'Q'}) for dr, dc in [(1,1),(1,-1),(-1,1),(-1,-1)]):
            print("Success")
            return

        print("Fail")

    except Exception:
        print("Fail")
