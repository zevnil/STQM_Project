import tensorflow as tf
def processing(D_PR_R_matrix, D_F_PR_R_matrix, D_PR_F_PR_R_matrix, dev, rev):
    no_of_paths = 3
    no_of_rev = len(rev)
    no_of_dev = len(dev)
    no_of_iter = 5

    tensor1 = tf.convert_to_tensor(D_PR_R_matrix)
    tensor2 = tf.convert_to_tensor(D_F_PR_R_matrix)
    tensor3 = tf.convert_to_tensor(D_PR_F_PR_R_matrix)
    tensor = tf.stack([tensor1, tensor2, tensor3], axis = 0)

    print("Initial tensor:")
    print(tensor)
    sum_rows = tf.reduce_sum(tensor, axis=2)
    sum_rows = tf.reshape(sum_rows, (no_of_paths,-1,1))
    T =  tensor / sum_rows
    print("T: ")
    print(T)

    sum_cols = tf.reduce_sum(tensor, axis=1)
    sum_cols = tf.reshape(sum_cols, (no_of_paths,1,-1))
    F = tensor/sum_cols
    print("F: ")
    print(F)

    sum_paths = tf.reduce_sum(tensor, axis=0)
    sum_paths = tf.reshape(sum_paths, (1,no_of_dev,-1))
    # print('sum_paths')
    # print(sum_paths)
    R = tensor/sum_paths
    R = tf.where(tf.math.is_nan(R), tf.ones_like(R) * 0, R)
    print("R: ")
    print(R)
    xt = tf.ones([no_of_dev, 1]) # Developer
    xt /= no_of_dev
    yt = tf.ones([no_of_paths, 1]) # Paths
    yt = yt/no_of_paths
    zt = tf.ones([no_of_rev, 1]) # Reviewer
    zt = zt/no_of_rev
    xt = tf.cast(xt, dtype = tf.float64)
    yt = tf.cast(yt, dtype = tf.float64)
    zt = tf.cast(zt, dtype = tf.float64)
    for i in range(no_of_iter):
        xt = tf.reshape(tf.tensordot(tf.tensordot(tf.transpose(yt),F, axes = 1), zt, axes = 1), [-1, 1])
        yt = tf.reshape(tf.tensordot(tf.reshape(tf.tensordot(R, zt, axes = 1),[no_of_paths, -1]), xt, axes = 1),[-1, 1])
        # yt = tf.tensordot(R, zt, axes = 1)
        zt = tf.reshape(tf.tensordot(tf.transpose(tf.reshape(tf.tensordot(tf.transpose(yt), R, axes = 1),[no_of_dev, -1])), xt, axes = 1),[-1, 1])
        
        # zt = tf.tensordot(tf.reshape(tf.tensordot(tf.transpose(yt), R, axes = 1),[no_of_paths, -1]), xt, axes = 1)
        print('xt: ')
        print(xt)
        print('yt: ')
        print(yt)
        print('zt: ')
        print(zt)
        print('--------------------------------------------------------------------------------------------------------------------------------')