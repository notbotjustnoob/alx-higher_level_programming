#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject list
 */
void print_python_list(PyObject *p)
{
    long int size, alloc, i;
    PyObject *item;
    PyListObject *list = (PyListObject *)p;

    printf("[*] Python list info\n");

    if (!PyList_Check(list))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_GET_SIZE(p);
    alloc = list->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < size; i++)
    {
        item = PyList_GET_ITEM(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

/**
 * print_python_bytes - Prints basic info about Python byte objects
 * @p: PyObject byte object
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *string;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", string);
    printf("  first %zd bytes:", (size < 10) ? size + 1 : 10);

    for (i = 0; i < (size < 10 ? size + 1 : 10); i++)
    {
        printf(" %02hhx", string[i]);
    }

    printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects
 * @p: PyObject float object
 */
void print_python_float(PyObject *p)
{
    double val;

    printf("[.] float object info\n");

    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    val = PyFloat_AsDouble(p);
    printf("  value: %lf\n", val);
}

#ifndef Py_LIMITED_API
PyMODINIT_FUNC PyInit_libPython(void)
{
    PyObject *m;

    m = PyModule_Create(&libPythonmodule);
    if (m == NULL)
        return NULL;

    return m;
}
#endif
