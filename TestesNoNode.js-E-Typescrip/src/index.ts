import express, { Request, Response } from 'express';
import { config } from 'dotenv'
import path from 'path'
import { readFileSync } from 'fs'

interface IUser{
    name: string
    age: number
}

config()
const app = express()
app.use('/client', express.static(path.join(__dirname, 'public')))
const url = process.env.API_BASE_URL ?? 'http://localhost'
const port = process.env.API_PORT ?? 3400
const users: IUser[] = [
    {
        name: 'Samuel',
        age: 2
    },
    {
        name: 'Ruan',
        age: 29
    }
]

app.get('/api', (req: Request, res: Response) => {
    //const homePagePath = path.join(__dirname, 'home.html')
    //const homePage = readFileSync(homePagePath)
 res.status(200).send('<h1 style="color: blue;">Samuel, filho amado do pai.</h1>');
 //res.status(200).send(homePage);
});

app.get('/api/users', (req: Request, res: Response) => {
 res.json(users);
 
})

app.listen(port, () => {
  console.log(`Servidor rodando no endereço ${url}:${port}`);
});
