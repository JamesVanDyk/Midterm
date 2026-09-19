How it works

1. Enter what user number you are (either 1 or 2)
2. It will create a symmetric shared key
3. Enter the message you would like to send to other user
4. It will encrypt your message and save it to public.txt
5. It will take the encrypted message from public.txt to hash it then encrypt it again to make a signature saved in encryptedFile.txt
6. It takes the original encrypted message in the public.txt file and hash it
7. Next it decrypt the second encryption from the encryptedFile.txt and compare it to the public.txt's hash and if they are equal
   it will make the verified variable equal to True
8. Once verified equals True, It takes the encrypted message from the public.txt file and decrypts it and saves the message to the
   user's file for them to view

----------------------------------------------------------------------------------------------------------------------------------------

Confidentiality:
The user has to put in their ID to write a message to the other.

Integrity:
A digital signature is used to make sure the message hasn't been changed while being sent.

Availability:
The user just has to look at their document to see what messages they have.

----------------------------------------------------------------------------------------------------------------------------------------

Key generation:

The key is generated for each user, then it is put through an algorithem to create a shared key that is only available for that session.
Once the session is ended, the next session will be replaced with a new one, because the key isn't saved on any files. The shared key
algorithem is symmetric because they each use only one private key and use them to make a new shared key that only each other knows.
This shared key is used for encryption and decryption from each party.