#!/bin/python3
# -*- coding: utf-8 -*-
import sqlite3
import os
__all__ = ["UsersData"]

class UsersData():
    def __init__(self, datapath = 'data.sqlite3'):
        self.connection = sqlite3.connect(datapath)
        self._init_tables()


    def _init_tables(self):
        #initialisating tables
        cursor = self.connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
        UserID INTEGER NOT NULL PRIMARY KEY,
        Gender TEXT NOT NULL
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS AnswerOrders (
        AnswerOrder INTEGER NOT NULL DEFAULT 0,
        UserID INTEGER NOT NULL,
        FOREIGN KEY(UserID) REFERENCES Users(UserID)
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Statuses (
        Timestamp DATETIME DEFAULT current_timestamp,
        StatusName TEXT NOT NULL,
        UserID INTEGER NOT NULL,
        FOREIGN KEY(UserID) REFERENCES Users(UserID)
        );
        ''')

        cursor.close()
        self.connection.commit()


    def create_user(self, userid, gender, status):
        #Create user
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Users (UserID, Gender) VALUES (?,?);", (userid, gender))
        cursor.execute("INSERT INTO Statuses (UserID, StatusName) VALUES (?,?);", (userid, status))
        cursor.execute("INSERT INTO AnswerOrders (AnswerOrder,UserID) VALUES (?,?);", (0,userid))
        cursor.close()
        self.connection.commit()


    def get_status(self, userid):
        #Get user status
        cursor = self.connection.cursor()

        cursor.execute("SELECT StatusName FROM Statuses WHERE Statuses.UserID = ?", (userid,))
        user_status = cursor.fetchone()
        user_status = user_status[0] if user_status else None

        cursor.execute("SELECT AnswerOrder FROM AnswerOrders WHERE AnswerOrders.UserID = ?", (userid,))
        answer_order = cursor.fetchone()
        answer_order = answer_order[0] if answer_order else None

        cursor.execute("SELECT Timestamp FROM Statuses WHERE Statuses.UserID = ?", (userid,))
        timestamp = cursor.fetchone()
        timestamp = timestamp[0] if timestamp else None

        cursor.close()
        return user_status, answer_order, timestamp


    def update_status(self, userid, user_status, answer_order=None, timestamp=None):
        #Update user status
        cursor = self.connection.cursor()

        cursor.execute("UPDATE Statuses SET StatusName = ?  WHERE Statuses.UserID= ? ", (user_status, userid))

        if answer_order:
            cursor.execute("UPDATE AnswerOrders SET Order = ?  WHERE AnswerOrders.UserID= ? ", (answer_order, userid))

        if timestamp:
            cursor.execute("UPDATE Statuses SET Timestamp = ?  WHERE Statuses.UserID= ? ", (timestamp, userid))

        cursor.close()
        self.connection.commit()


    def add_answer(self, userid):
        #Update user status
        cursor = self.connection.cursor()

        cursor.execute("SELECT AnswerOrder FROM AnswerOrders WHERE AnswerOrders.UserID = ?", (userid,))
        answer_order = cursor.fetchall()[0][0]
        answer_order+=1
        cursor.execute("UPDATE AnswerOrders SET AnswerOrder = ?  WHERE AnswerOrders.UserID= ? ", (answer_order, userid))
        cursor.close()
        self.connection.commit()






        # Additions tables
        # cursor.execute('''
        # CREATE TABLE IF NOT EXISTS Tests (
        # TestID INTEGER PRIMARY KEY autoincrement,
        # TestName TEXT NOT NULL UNIQUE
        # );
        # ''')
        #
        # cursor.execute('''
        # CREATE TABLE IF NOT EXISTS PsychotypesSystems (
        # SystemID INTEGER PRIMARY KEY autoincrement,
        # SystemName TEXT NOT NULL UNIQUE
        # );
        # ''')
        #
        # cursor.execute('''
        # CREATE TABLE IF NOT EXISTS TestSessions (
        # SessionID INTEGER PRIMARY KEY autoincrement,
        # Timestamp DATETIME DEFAULT current_timestamp,
        # PsychotypesSystemID INTEGER NOT NULL DEFAULT 0,
        # TestID INTEGER NOT NULL DEFAULT 0,
        # UserID INTEGER NOT NULL,
        # FOREIGN KEY(PsychotypesSystemID) REFERENCES PsychotypesSystems(SystemID),
        # FOREIGN KEY(TestID) REFERENCES Tests(TestID),
        # FOREIGN KEY(UserID) REFERENCES Users(UserID)
        # );
        # ''')

        # cursor.execute('''
        # CREATE TABLE IF NOT EXISTS TestSessions (
        # SessionID INTEGER PRIMARY KEY autoincrement,
        # Timestamp DATETIME DEFAULT current_timestamp,
        # UserID INTEGER NOT NULL,
        # FOREIGN KEY(UserID) REFERENCES Users(UserID)
        # );
        # ''')
        #
        # cursor.execute('''
        # CREATE TABLE IF NOT EXISTS Answers (
        # AnswerID INTEGER PRIMARY KEY autoincrement,
        # Timestamp DATETIME DEFAULT current_timestamp,
        # SessionID INTEGER NOT NULL,
        # Vector TEXT NOT NULL,
        # FOREIGN KEY(SessionID) REFERENCES TestSessions(SessionID)
        # );
        # ''')

        # cursor.execute('''
        # CREATE view if not exists UserStatuses as
        # SELECT
        # Users.UserTelegramID,
        # Statuses.Timestamp,
        # Statuses.StatusName
        # FROM
        # Users,
        # Statuses
        # WHERE
        # Users.UserID = Statuses.UserID;
        # ''')
