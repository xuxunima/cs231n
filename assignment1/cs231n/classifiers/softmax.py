import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = X.shape[0]
  num_class = W.shape[1]
  for i in range(num_train):
    score = np.dot(X[i,:],W)
    exp_score = score-np.max(score)
    exp_score = np.exp(exp_score)
    s = exp_score / np.sum(exp_score)
    loss -= np.log(s[y[i]])
    for j in range(num_class):
        if j == y[i]:
            dW[:,j] += (s[j]-1) * X[i,:].T
        else:
            dW[:,j] += s[j] * X[i,:].T
  loss /= num_train
  loss += reg * np.sum(W * W)
  dW /= num_train
  dW += reg * 2 * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = X.shape[0]
  num_class = W.shape[1]
  Y = np.zeros((num_train,num_class))
  Y[np.arange(num_train),y] = 1
  score = np.dot(X,W)
  score -= np.max(score,axis=1,keepdims=True)
  exp_score = np.exp(score) / np.sum(np.exp(score),axis=1,keepdims=True)
  loss = -np.sum(np.log(exp_score)* Y) / num_train
  dW = np.dot(X.T, exp_score - Y) / num_train
  loss += reg * np.sum(W * W)
  dW += reg * 2 * W  
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

