<!-- python -m autopep8 --max-line-length 60 --in-place --aggressive --aggressive ./**.py -->

# Budget Planning - API
In this repo there's only the API and Back-End of the this project.

## Install and run the project
```sh
# install
virtualenv --python=python3 .virenv
source ./virenv/bin/activate
pip install -r requirements.txt

# create 1º super user
python manage.py createsuperuser

# run
cd djangoUserAuth
python manage.py runserver
```

## Project Requirements
1. Manage user's **access control** to the system
   1. The user's can be:
      1. Super user ─ there can be only one
      2. Guest ─ can only see the data
      3. Trusty ─ can do everythig in the sytstem, except deleting it and changing the user user.
   2. The user must have the power of giving the super user power to another user.
2. Manage **Incomes**
   1. Date of the Income
   2. Recurrency of the Income
   3. etc...
3. Manage **Bill**
   1. Date of the Income
   2. Recurrency of the Income
   3. The user can classify each bill, as a tag.
   4. A bill is always associated with a *Transference* in an Account or with a *Cred Card*
4. The user must be capable if **deviding a bill** between this user and other people that he will indicate.
5. Manage **Borrowing**
   1. By who?
   2. When is it going to be paind?
   3. How much is it going to be payed per time (per mounth, week, etc...)
6. Manage **Savings**
7. **BI**, that is, the system must be capable of showing some basic statistic charts for the user
8. Manager **Account**:
   1. Managing **Transferences** in an account. They can be made:
      1. Between *Accounts*
      2. To pay some *Bill*
      3. From an Income
      4. From a *Borrowing* payment
      5. The money the user has in his pocket is considered to be a type of account.
9. Manage **Cred Cards**
   1.  Cards has **model of use**:
       1.  Credit
       2.  Debit
