from typing import Dict, List, Tuple
import cv2
import numpy as np
from image_processors.ImageProcessor import ImageProcessor


class ShapeSelector(ImageProcessor):
    def __init__(self):
        super().__init__()
        
    def __call__(self, img: cv2.Mat, scores:List[Dict[str, float]], warps:List[cv2.Mat], trapezoids:np.ndarray[np.float_]) -> Tuple[List[int], List[np.ndarray[np.float_]], List[float]]:
        """Classifies shapes.
        This function SHOULD add an entry in the scores called 'valid' indicating the total score.
        This ensures compatibility with the accuracy benchmark.

        Args:
            img (cv2.Mat): Input image, used for debugging.
            scores (List[Dict[str, float]]): Scores per trapezoid (length of n).
            warps (List[cv2.Mat]): Warps for each trapezoid. Shape is (n, height of n, width of n)
            trapezoids (np.ndarray[np.float_]): Trapezoids on which data is based. Shape is (n, 4, 2)

        Returns:
            Tuple[List[int], List[np.ndarray[np.float_]], List[float]]: (indices, selectedTrapezoids, scores)
            
            indicies (List[int]): List of indices such that selectedTrapezoids[i] == trapezoids[indices[i]] (length of m).
            selectedTrapezoids (List[np.ndarray[np.float_]]): List of selected trapezoids (length of m, shape of (4, 2)).
            scores (List[float]): List of scores (length of m).
        """