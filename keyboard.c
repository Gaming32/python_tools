#include <Python.h>
#include <conio.h>

static PyObject *
is_pressed_any(PyObject *self, PyObject *args)
{
    /* is any key pressed */
    if (PyArg_ParseTuple(args, ""))
        return PyArg_BuildValue("i", kbhit());
    else
        return NULL;
}

static PyObject *
is_pressed(PyObject *self, PyObject *args)
{
    char *hope;
    if (PyArg_ParseTuple(args, "s", &hope))
    {
        char key = getch();
        if (key == hope)
            Py_RETURN_TRUE;
        else
            Py_RETURN_FALSE;
    }
    else
        return NULL;
}

static PyObject *
is_released(PyObject *self, PyObject *args)
{
    char *hope;
    if (PyArg_ParseTuple(args, "s", &hope))
    {
        char key = getch();
        if (key != hope)
            Py_RETURN_TRUE;
        else
            Py_RETURN_FALSE;
    }
    else
        return NULL;
}


static PyMethodDef keyboard_methods[] = {
    {"is_pressed_any", is_pressed_any, METH_VARARGS, NULL},
    {"is_pressed",     is_pressed,     METH_VARARGS, NULL},
    {"is_released",    is_released,    METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef keyboardmodule = {
    PyModuleDef_HEAD_INIT,
    "keyboard",
    NULL,
    -1,
    keyboard_methods
};

PyMODINIT_FUNC
PyInit_keyboard()
{
    return PyModule_Create(&keyboardmodule)
}