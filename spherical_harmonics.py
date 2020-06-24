def K_l_m(l,m):
    """
    Computes the constant pre-factor for the spherical harmonic of degree l and order m
    input:
    l: int, l>=0
    m: int, -l<=m<=l
    """
    return ((2*l+1)*np.math.factorial(l-abs(m))/(4*np.pi*np.math.factorial(l+abs(m))))**0.5
    
def sin_cos_expressions(m): 
    S_m = [0]
    C_m = [1]

    for i in range(1,m+1):
        S_m += [x*S_m[i-1] + y*C_m[i-1]]
        C_m += [x*C_m[i-1] - y*S_m[i-1]]
    return S_m, C_m
    
def associated_legendre_polynomials(l,m):
    P_l_m = [[0]*(j+1) for j in range(m+1)]
    P_l_m[0][0]=1
    P_l_m[1][0]=z
    for j in range(2,l+1):
        P_l_m[j][0] = sym.simplify(((2*j-1)*z*P_l_m[j-1][0] - (j-1)*P_l_m[j-2][0])/j)
    for i in range(1,m):
        P_l_m[i][i]   = sym.simplify((1-2*i)*P_l_m[i-1][i-1])
        P_l_m[i+1][i] = sym.simplify((2*i+1)*z*P_l_m[i][i])
        for j in range(i+2,l+1):
            P_l_m[j][i] = sym.simplify(((2*j-1)*z*P_l_m[j-1][i] - (i+j-1)*P_l_m[j-2][i])/(j-i))
    
    P_l_m[m][m] = sym.simplify((1-2*m)*P_l_m[m-1][m-1])
    return P_l_m
