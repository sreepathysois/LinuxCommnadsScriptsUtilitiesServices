# Compiler and flags
CC = gcc
CFLAGS = -Iinclude -Wall -O2

# Directories
SRCDIR = src
INCDIR = include
OBJDIR = build
TARGET = app

# Object files
OBJS = $(OBJDIR)/main.o $(OBJDIR)/math.o $(OBJDIR)/io.o

.PHONY: all clean

# Default target
all: $(TARGET)

# Link the executable
$(TARGET): $(OBJS)
	$(CC) -o $@ $^

# Compile each .c file to .o file
$(OBJDIR)/%.o: $(SRCDIR)/%.c
	@mkdir -p $(OBJDIR)
	$(CC) $(CFLAGS) -c $< -o $@

# Clean all compiled files
clean:
	rm -rf $(OBJDIR)/*.o $(TARGET)
