import numpy as np

class Board():
	# Rook
	# Knight
	# Queen
	# King
	# Pawn
	# board centric for clearing board and board state
	# piece centric better for calculations in board pieces movement
	""""
		np.array() representation
		[0,0,0...1,0...0]
		[a1.......h8]

		- function to set starting state
		- function to map from geometric to bitmap
	//	- function to bitwise and all bitmaps >> board state
		- function to map fen >> board state fen starting string position
			// fen string


		-- 
		function to bitwise AND all bitmaps for interjecting pos | piece capture | illegal moves 
	"""

	def __init__(self):
		self.white_rook_bitboard=self.create_empty_bitmap()
		self.white_king_bitboard=self.create_empty_bitmap()
		self.white_bishop_bitboard=self.create_empty_bitmap()
		self.white_pawn_bitboard=self.create_empty_bitmap()
		self.white_knight_bitboard=self.create_empty_bitmap()
		self.white_queen_bitboard=self.create_empty_bitmap()

		self.black_rook_bitboard=self.create_empty_bitmap()
		self.black_king_bitboard=self.create_empty_bitmap()
		self.black_bishop_bitboard=self.create_empty_bitmap()
		self.black_pawn_bitboard=self.create_empty_bitmap()
		self.black_knight_bitboard=self.create_empty_bitmap()
		self.black_queen_bitboard=self.create_empty_bitmap()

		self.bitboards=np.vstack(
			self.white_bishop_bitboard,
			self.white_king_bitboard,
			self.white_knight_bitboard,
			self.white_rook_bitboard,
			self.white_queen_bitboard,

			self.black_rook_bitboard,
			self.black_bishop_bitboard,
			self.black_knight_bitboard,
			self.black_queen_bitboard,
			self.black_queen_bitboard
		)
		self.init_pieces()

	def get_bitboard_state(self):
		result=np.zeros(64,dtype="byte")

		for board in self.bitboards:
			result=np.bitwise_or(board,result,dtype="byte")
		self.bitboards=result



	def create_empty_bitmap(self):
		# return [0 for _ in create_empty_bitmap()]
		# return 64*[0]
		return np.zeroes(64,dtype="byte")

	# intial board posi	
	def init_pieces(self):
		self.white_rook_bitboard[0]=1
		self.white_rook_bitboard[7]=1
		self.white_knight_bitboard[1]=1
		self.white_knight_bitboard[6]=1
		self.white_bishop_bitboard[2]=1
		self.white_bishop_bitboard[5]=1
		self.white_queen_bitboard[4]=1
		self.white_king_bitboard[4]=1

		for i in range(8,15):
			self.white_pawn_bitboard[i]=1

		self.black_rook_bitboard[63]=1
		self.black_rook_bitboard[56]=1
		self.black_knight_bitboard[57]=1
		self.black_knight_bitboard[62]=1
		self.black_bishop_bitboard[61]=1
		self.black_bishop_bitboard[58]=1
		self.black_queen_bitboard[59]=1
		self.black_king_bitboard[60]=1
		
		for i in range(8,15):
			self.black_pawn_bitboard[i]=1

