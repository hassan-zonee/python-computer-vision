{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "42368b5d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ac93438c",
   "metadata": {},
   "outputs": [],
   "source": [
    "cap = cv2.VideoCapture('testvid.mp4')\n",
    "\n",
    "while True:\n",
    "    ret, frame = cap.read()\n",
    "\n",
    "    if not ret:\n",
    "        break\n",
    "\n",
    "    cv2.imshow('Video', frame)\n",
    "\n",
    "    if(cv2.waitKey(1) and 0xff == ord('q')):\n",
    "        break\n",
    "\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "env",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
