import chess

def san_to_lan(pgn):
    board = chess.Board()
    lan_moves = []
    for san in pgn:
        try:
            move = board.parse_san(san)  # Parses the SAN move.
            # Constructing LAN from move object.
            lan = board.uci(move)  # Converts move to Universal Chess Interface (UCI) format, which resembles LAN.
            board.push(move)  # Pushes the move to update the board's state.
            lan_moves.append(lan)
        except ValueError as e:
            # Handles illegal or impossible moves.
            return {"error": f"Illegal or impossible move '{san}': {str(e)}", "board": board.fen()}
    return lan_moves
