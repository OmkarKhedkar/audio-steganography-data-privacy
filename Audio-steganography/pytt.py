import matlab.engine
import  random
def embedder():
	eng = matlab.engine.start_matlab()
	eng.data_embedding_lsb(nargout=0)
	
embedder()