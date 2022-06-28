import numpy as np
import time

N = 4092
if __name__ == "__main__":
    #n^2 in memory
    A = np.random.randn(N, N).astype(np.float32)
    
    #N^2 in memory
    B = np.random.randn(N, N).astype(np.float32)
    
    #N^2 outputs cells with 2N compute each
    flop = N*N*2*N
    print(f"{flop / 1e9:.2f} GFLOP")   #which is flops floating point operation.s per sec
    
    st = time.monotonic()
    C = A @ B
    et = time.monotonic()
    s = et - st
   
    print(f"{flop/s * 1e-9} GFLOPS")
    
    
    
    
    
    
    
    
    
    
    
